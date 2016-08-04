from flablo import db
from werkzeug.security import generate_password_hash, check_password_hash

class DBTest(db.Model):
    __tablename__='test'
    ID = db.Column(db.Integer, primary_key=True)
    test_content = db.Column(db.String(20))


class User(db.Model):
    __tablename__='users'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64),unique=True)
    password_hash = db.Column(db.String(128))

    @property
    def password(self):
        raise "you cant read it"

    @password.setter
    def password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password_hash(self,password):
        return check_password_hash(self.password_hash, password)

    def __init__(self , username ,password):
        self.username = username
        self.password_hash = generate_password_hash(password)

    @property
    def is_authenticated(self):
        return True

    @property
    def is_active(self):
        return True

    @property
    def is_anonymous(self):
        return False

    def get_id(self):
        # python 2
        return unicode(self.id)
        # python 3
        # return str(self.id)  

    def __repr__(self):
        return '<User %r>' % (self.username)
        
