from flask import render_template, flash, redirect, url_for
from app import app
from app.forms import LoginForm
from app.models import User
from flask_login import current_user, login_user, logout_user

@app.route('/')
@app.route('/index')
def index():
   user = {'username' : 'Sneh'}
   songs = [
      {
         'author' :'this',
         'title': 'that',
         'url' : 'url'
      },
      {
         'author' :'lap',
         'title': 'top',
         'url' : 'url2'
      },
   ]
   return render_template('index.html',title='Home', user=user, songs=songs)

   
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
      return redirect(url_for('index'))
   return render_template('login.html', form=form, title='Sign In')

@app.route('/logout')
def logout():
   logout_user()
   return redirect(url_for('index'))