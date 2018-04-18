import os
import sqlite3
import config
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

app = Flask(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_object(config)

@app.route('/')
def index():
    # print(url_for('article',id='123'))
    # return 'Index Page!'
    args = {
        'name':'Shepherd',
        'addr':'Mars'
    }
    return render_template('index.html', **args)

@app.route('/article/<id>')
def article(id):
    return '您请求的参数是：%s' % id

@app.route('/user/<is_login>')
def user(is_login):
    if is_login == '1':
        return '欢迎来到用户中心'
    else:
        login_url = url_for('login')
        return redirect(login_url)  

@app.route('/login/')
def login():
    return render_template('login.html')

def connect_db():
    """Connects to the specific database."""
    rv = sqlite3.connect(app.config['DATABASE'])
    rv.row_factory = sqlite3.Row
    return rv

def init_db():
    with app.app_context():
        db = get_db()
        with app.open_resource('schema.sql', mode='r') as f:
            db.cursor().executescript(f.read())
        db.commit()

if __name__ == '__main__':
    app.run()