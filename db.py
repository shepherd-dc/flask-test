import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# db.create_all()

# user表
# create table user (
#     id int primary key auto_increment,
#     username varchar(100) not null,
#     password varchar(32) not null
# )

# article表：
# create table article (
#     id int primary key auto_increment,
#     title varchar(100) not null,
#     content text not null,
#     author_id int,
#     foreign key `author_id` references `user.id`
# )
class User(db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(100), nullable=False)
    password = db.Column(db.String(32), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    author = db.relationship('User', backref=db.backref('articles'))

db.create_all()

@app.route('/')
def index():
    # article = Article(title='哈萨克和', content='的数据阿拉基')
    # article.author = User.query.filter(User.id == 1).first()
    # print(article.author.username)
    # db.session.add(article)
    # db.session.commit()

    author1 = User.query.filter(User.username == 'shepherd').first()
    articles = author1.articles
    for article in articles:
        print(article.title)

    # # 增：
    # article1 = Article(title='headline', content='正文内容111')
    # db.session.add(article1)
    # db.session.commit()

    # # 查：
    # article1 = Article.query.filter(Article.id==1).first()
    # print('title:%s' % article1.title)
    # print('content:%s' % article1.content)

    # # 改：
    # article1 = Article.query.filter(Article.title=='headline').first()
    # article1.title = 'new title'
    # db.session.commit()

    # # 删：
    # article1 = Article.query.filter(Article.title=='headline').first()
    # db.session.delete(article1)
    # db.session.commit()

    return 'SQLAlchemy CURD'

if __name__ == '__main__':
    app.run()