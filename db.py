import config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config.from_object(config)
db = SQLAlchemy(app)
# db.create_all()

# article表：
# create table article (
#     id int primary key auto_increment,
#     title varchar(100) not null,
#     content text not null
# )
class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)

db.create_all()

@app.route('/')
def index():
    # 增：
    article1 = Article(title='headline', content='正文内容111')
    db.session.add(article1)
    db.session.commit()

    # # 查：
    # article1 = Article.query.filter(Article.id==1).first()
    # print('title:%s' % article1.title)
    # print('content:%s' % article1.content)

    # # 改：
    # article1 = Article.query.filter(Article.title=='headline').first()
    # article1.title = 'new title'
    # db.session.commit()

    # 删：
    # article1 = Article.query.filter(Article.title=='headline').first()
    # db.session.delete(article1)
    # db.session.commit()

    return 'SQLAlchemy CURD'

if __name__ == '__main__':
    app.run()