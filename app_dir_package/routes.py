from flask import render_template
from app_dir_package import app
from app_dir_package.forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Miguel'}
    posts = [
        {
            'author': {'username': 'John'},
            'body': 'Beutiful day in Portland',
        },
        {
            'author': {'username': 'Susan'},
            'body': 'The Aventures movie was so cool!',
        },
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title='Sign In', form=form)