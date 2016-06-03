from flablo import app, db
from flask import render_template
from flablo.models import DBTest

@app.route('/')
def hello():
    return "Hello World"

@app.route('/dbtest')
def dbtest():
    test_data = DBTest.query.filter(DBTest.ID > 1).all()
    return render_template("dbtest.html", data = test_data)
