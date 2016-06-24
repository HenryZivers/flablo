from flablo import app, db
from flask import render_template, request, redirect, url_for, flash
from flablo.models import DBTest, Todo

@app.route('/')
def index():
    return "Hello Flablo!"

@app.route('/dbtest')
def dbtest():
    test_data = DBTest.query.filter(DBTest.ID > 1).all()
    return render_template("dbtest.html", data = test_data)

@app.route('/newtodo', methods = ['GET', 'POST'])
def newtodo():
    if request.method == 'POST':
        todo = Todo(request.form['title'], request.form['text'])
        db.session.add(todo)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('newtodo.html')
    #return "new todo"
