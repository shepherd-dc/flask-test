from flask import Flask, session
import os
from datetime import timedelta

app = Flask(__name__)
app.config['SECRET_KEY'] = os.urandom(24)
app.config['PERMANENT_SESSION_LIFETIME'] = timedelta(days=7)

@app.route('/')
def hello_world():
    session['username'] = 'shepherd'
    # 如果没有制定session的过期时间，默认是浏览器关闭后自动过期
    # 如果设置session的permanent属性为True，而没有设置config中的PERMANENT_SESSION_LIFETIME,过期时间为1个月
    session.permanent = True
    return 'Hello World!'

@app.route('/get/')
def get():
    # session['username']
    return session.get('username')

@app.route('/delete/')
def delete():
    session.pop('username')
    # del session['username']  
    return 'successfully deleted'

@app.route('/clear/')
def clear():
    session.clear()
    return 'successfully cleared'

if __name__ == '__main__':
    app.run(debug=True)