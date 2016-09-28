import os

basedir = os.path.abspath(os.path.dirname(__file__))

SECRET_KEY = ''

# mysql-python / mysqldb
SQLALCHEMY_DATABASE_URI = 'mysql+mysqldb://<user_name>:<user_pass>@localhost/<db_name>'
# pymysql
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://<user_name>:<user_pass>@localhost/<db_name>'

SQLALCHEMY_MIGRATE_REPO = os.path.join(basedir, 'db_repository')
SQLALCHEMY_TRACK_MODIFICATIONS = True
