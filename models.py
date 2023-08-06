from peewee import *

db = SqliteDatabase('articles.db')


class BaseModel(Model):
    id = PrimaryKeyField(unique=True)

    class Meta:
        database = db
        order_by = 'id'


class Article(BaseModel):
    name = CharField()
    content = TextField()

    class Meta:
        db_table = 'articles'


class Comment(BaseModel):
    content = TextField()
    article_id = ForeignKeyField(Article)

    class Meta:
        db_table = 'comments'






