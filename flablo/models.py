from flablo import db

class DBTest(db.Model):
    __tablename__='test'
    ID = db.Column(db.Integer, primary_key=True)
    test_content = db.Column(db.String(20))

class Todo(db.Model):
    __tablename__='todos'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(60))
    text = db.Column(db.Text)
    done = db.Column(db.Boolean)
    updated = db.Column(db.DateTime)

    def __init__(self, title, text):
        self.title = title
        self.text = text
        self.done = False
        self.updated = datetime.utcnow()

    def __repr__(self):
        return '<Todo %r>' % (self.title)
