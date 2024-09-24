from flask import render_template, redirect, url_for, session, flash
from flask import Flask, request

from forms.login_form import LoginForm
from forms.register_form import RegistrationForm

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import DeclarativeBase

class Base(DeclarativeBase):
  pass

db = SQLAlchemy(model_class=Base)

# create the app
app = Flask(__name__)
# configure the SQLite database, relative to the app instance folder
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///project.db"
# initialize the app with the extension
db.init_app(app)

from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column

class User(db.Model):
    id: Mapped[int] = mapped_column(primary_key=True)
    username: Mapped[str] = mapped_column(unique=True)
    password: Mapped[str]

app = Flask(__name__)


@app.route("/")
def home():
    return render_template('_base.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


user_database = {
    "vasyl": "1",
    "vlad": "12",
    "anya": "123"
}

app.secret_key = 'KEY'


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return render_template('show_posts.html', post_id=post_id)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'POST' and form.validate():
        username = request.form['username']
        password = request.form['password']
        if username in user_database and user_database[username] == password:
            session['username'] = username
            flash("You successfuly logged")
            return redirect(url_for('hello_user', username=request.form['username']))

    return render_template('login.html', form=form)



@app.route('/logout')
def logout():
    session.pop('username', None)

    return redirect(url_for('home'))


@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm(request.form)
    if request.method == 'POST' and form.validate():
        flash('Thanks for register')
        return redirect(url_for('login'))
    return render_template('register.html', form=form)



@app.route("/user/<username>")
def hello_user(username):
    if 'username' in session and session['username'] == username:
        return render_template('hello_user.html', username=username)
    else:
        return render_template('login.html')

@app.route('/users')
def show_users_profile():
    users = [
        'vlad',
        'anya',
        'sovyak'
    ]
    return render_template('user_list.html', users=users)


@app.route('/about')
def about():
    return render_template('about.html')


if __name__ == '__main__':
    app.run(debug=True)

