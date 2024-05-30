from flask import render_template
from flask import Flask
app = Flask(__name__)


@app.route("/")
def home():
    return render_template('home.html')


@app.route("/posts")
def posts():
    return render_template('posts.html', posts=range(1, 11))


@app.route('/posts/<int:post_id>')
def show_post(post_id):
    return render_template('show_posts.html', post_id=post_id)


@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/register')
def register():
    return render_template('register.html')

@app.route('/about')
def about():
    return render_template('about.html')


@app.route("/user/<username>")
def hello_user(username):
    return render_template('hello_user.html', username=username)


@app.route('/users')
def show_users_profile():
    users = [
        'Kyznetsow',
        'Vlad',
        'Serhiy',
        'Anya'
    ]
    return render_template('user_list.html', users=users)
