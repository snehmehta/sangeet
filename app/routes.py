from flask import render_template, flash, redirect, url_for, request, send_from_directory
from app import app
from app import db
from app.forms import LoginForm, RegistrationForm, SongForm
from app.models import User, Song
from flask_login import current_user, login_user, logout_user, login_required
from werkzeug.urls import url_parse
from werkzeug.utils import secure_filename
import os 
import audio_metadata
from app import helpers

ALLOWED_EXTENSIONS = {'mp3'}

def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

def gen(song):
   
   with open(song, "rb") as f:
      print(song) # DEBUG
      data = f.read(1024)
      while data:
         yield data
         data = f.read(1024)


@app.route('/',methods=['GET', 'POST'])
@app.route('/index',methods=['GET', 'POST'])
@login_required
def index():
   
   form = SongForm()

   if form.validate_on_submit():
      file = form.song.data
      if file and allowed_file(file.filename):
         filename = secure_filename(helpers.get_random_string(6)+'.mp3')
         filepath = os.path.join(app.config['UPLOAD_DIR'], filename)
         file.save(filepath)

         song = Song(title=file.filename, url=filename, listener=current_user)
         db.session.add(song)
         db.session.commit()
         return redirect(url_for('index'))
      else:
         flash('You can only upload mp3 for now')
   
   page = request.args.get('page',1,type=int)
   songs = current_user.songs.paginate(page, app.config['SONGS_PER_PAGE'], False)
   next_url = url_for('index', page=songs.next_num) \
      if songs.has_next else None
   prev_url = url_for('index', page=songs.prev_num) \
      if songs.has_prev else None

   return render_template('index.html',title='Home', songs=songs.items, form=form, next_url=next_url, prev_url=prev_url)

   
@app.route('/login', methods=['GET', 'POST'])
def login():

   if current_user.is_authenticated:
      return redirect(url_for('index'))

   form = LoginForm()
   if form.validate_on_submit():

      user = User.query.filter_by(username=form.username.data).first()
      if user is None or not user.check_password(form.password.data):
         flash('Invalid username or password')
         return redirect(url_for('login'))

      login_user(user, remember=form.remember_me.data)

      next_page = request.args.get('next')
      if not next_page or url_parse(next_page).netloc != '':
         next_page = url_for('index')
      
      return redirect(next_page)
   return render_template('login.html', form=form, title='Sign In')

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index'))

@app.route('/register', methods=['GET', 'POST'])
def register():
   
   if current_user.is_authenticated:
      return redirect(url_for('index'))

   form = RegistrationForm()

   if form.validate_on_submit():

      user = User(username=form.username.data, email=form.email.data)
      user.set_password(form.password.data)
      db.session.add(user)
      db.session.commit()

      flash('Congratulations ! you are a registered user now')

      return redirect(url_for('login'))

   return render_template('register.html', title='Register', form=form)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
   return render_template('play.html', url=os.path.join(app.config['UPLOAD_DIR'],
                               filename))
