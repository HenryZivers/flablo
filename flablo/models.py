from flablo import db

class DBTest(db.Model):
    __tablename__='test'
    ID = db.Column(db.Integer, primary_key=True)
    test_content = db.Column(db.String(64))


