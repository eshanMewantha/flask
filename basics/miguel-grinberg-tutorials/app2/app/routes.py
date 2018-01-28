from app import app
from flask import render_template

@app.route('/')
@app.route('/index')
def index():
    user = {'username': 'Stark'}
    posts = [
        {
            'author': {'username': 'Banner'},
            'body': 'Still working with gamma rays!'
        },
        {
            'author': {'username': 'Rodgers'},
            'body': 'I am the super soldier!'
        }
    ]
    return render_template('index.html', title='Home', user=user, posts=posts)