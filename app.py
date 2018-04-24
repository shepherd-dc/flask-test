import config
from flask import Flask, url_for, render_template, redirect, request, g, session
from exts import db
from models import User, Article
from utils import login_log

app = Flask(__name__)
# app.config.from_envvar('FLASKR_SETTINGS', silent=True)
app.config.from_object(config)

# 初始化数据模型
db.init_app(app)

# # 将app推栈到服务器，获得app上下文
# # 使用flask-migrater则不需要该映射
# with app.app_context():
#     db.create_all()

@app.route('/')
def index():
    # author1 = User.query.filter(User.username == 'shepherd').first()
    # articles = author1.articles
    # for article in articles:
    #     print(article.title)

    args = {
        'name':'Shepherd',
        'addr':'Mars'
    }
    return render_template('index.html', **args)

@app.route('/article/<id>')
def article(id):
    return '您请求的参数是：%s' % id

@app.route('/user/')
def user():
    # if session.get('username'):
    if hasattr(g, 'username'):
        return render_template('user.html')
    else:
        login_url = url_for('login')
        return redirect(login_url)  

# 默认的视图函数只能采用get请求，如果要使用post请求，需写明
@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        return render_template('login.html')
    else:
        username = request.form.get('username')
        password = request.form.get('password')
        if username == 'shepherd' and password == '123456':
            session['username'] = username
            session.permanent = True
            # g.username = username
            # login_log()
            return redirect(url_for('user')) 
        else:
            return '用户名或密码错误'

@app.before_request
def is_login():
    if session.get('username'):
        g.username = session.get('username')

@app.context_processor
def user_center():
    return {'uname':'carlos'}
        
@app.route('/search/')
def search():
    # print(request.args)
    q = request.args.get('q')
    return '查询关键字是：%s' % q
    print(q)

if __name__ == '__main__':
    app.run()