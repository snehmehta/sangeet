from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, FileField

from wtforms.validators import DataRequired, ValidationError, Email, EqualTo
from app.models import User, Song
from flask import request


class LoginForm(FlaskForm):

    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])

    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')

class RegistrationForm(FlaskForm):


    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()

        if user is not None:
            raise ValidationError('Please use a differen username.')

    def validate_email(self, email):

        user = User.query.filter_by(email=email.data).first()
        if user is not None:

            raise ValidationError('Please use a different email address')


class EditSongMeta(FlaskForm):

    title = StringField('Title', validators=[DataRequired()], render_kw={'disabled':''})
    artist = StringField('Artist')
    album = StringField('Album')
    submit = SubmitField('Submit')

class SongForm(FlaskForm):
    
    song = FileField('Song', validators=[DataRequired()])
    submit = SubmitField('Upload')


    def validate_song(self, song):
        from flask_login import current_user
        song = current_user.songs.filter_by(title=song.data.filename).first()
        if song is not None:

            raise ValidationError('Song already present')

class SearchForm(FlaskForm):

    q = StringField('Search', validators=[DataRequired()])

    def __init__(self, *args, **kwargs):
        if 'formdata' not in kwargs:
            kwargs['formdata'] = request.args
        if 'csrf_enabled' not in kwargs:
            kwargs['csrf_enabled'] = False
        super(SearchForm, self).__init__(*args, **kwargs)
