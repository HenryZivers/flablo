from flablo import app, db, login_manager
from flask import render_template, request, redirect, url_for, flash
from flablo.models import DBTest, User
from flask_login import login_user,logout_user,login_required
from .forms import LoginForm

@app.route('/')
def index():
    return "Hello Flablo!"


@app.route('/welcome')
def welcome():
    return "welcome!"

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        return render_template('register.html')
    user = User(request.form['username'], request.form['password'])
    db.session.add(user)
    db.session.commit()
    return redirect(url_for('login'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    form = LoginForm()
    print form.errors
    if form.validate_on_submit():
        user=User.query.filter_by(username=request.form['username']).first()
        if user is not None and user.check_password_hash(form.password.data):
            login_user(user)
            return redirect(url_for('welcome'))
        else:
            flash('Invalid username or password')
    return render_template('login.html',form=form)


@app.route('/logout', methods=['GET'])
@login_required
def logout():
    logout_user()
    flash('you have been logged out')
    return redirect(url_for('login'))



@app.route('/dbtest')
@login_required
def dbtest():
    test_data = DBTest.query.filter(DBTest.ID > 1).all()
    return render_template("dbtest.html", data = test_data)

