from flask import render_template, redirect, flash, url_for
from app import app
from app.models import Post, User
from app.forms import LoginForm


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        flash(f'Login requested for user {form.username.data}, remember_me={form.remember_me.data}')
        return redirect(url_for('index'))
    return render_template('login.html', title='Sign In', form=form)


@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Roma'}
    posts = [
        {
            'author': {'username': 'John', 'id': 1},
            'body': 'Beautiful day in Portland!'
        },
        {
            'author': {'username': 'Susan', 'id': 2},
            'body': 'The Avengers movie was so cool!'
        },
        {
            'author': {'username': 'Ипполит', 'id': 3},
            'body': 'Какая гадость эта ваша заливная рыба!!'
        }
    ]
    titles = Post.query.all()
    users = User.query.all()
    return render_template('index.html', title='Home', user=user, posts=posts, titles=titles, users=users)

