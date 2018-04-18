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
    return 'sqlalchemy'

if __name__ == '__main__':
    app.run()