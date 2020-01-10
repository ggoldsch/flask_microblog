from flask import render_template, flash, redirect, url_for
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

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        #print('FLASH!!!!')
        flash('Login requested for user {}, remember_me={}'.format(
            form.username.data, form.remember_me.data))
        return redirect(url_for('index'))    
    return render_template('login.html', title='Sign In', form=form)