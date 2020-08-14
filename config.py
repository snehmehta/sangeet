import os
basedir = os.path.abspath(os.path.dirname(__name__))
uploaddir = os.path.join(basedir,'app','static','music')

class Config(object):

    SECRET_KEY = os.environ.get('SECRET_KEY') or 'hehahfjio32nr0fhJ12@$@#!'
    
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    UPLOAD_DIR = uploaddir

    SONGS_PER_PAGE = 5