import config
from flask import Flask, url_for, render_template
from exts import db
from models import User, Article

app = Flask(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_object(config)

# 初始化数据模型
db.init_app(app)

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

if __name__ == '__main__':
    app.run()