from flask import Blueprint, request, Response
from models import *

article_bp = Blueprint('article', __name__)


@article_bp.route('/articles')
def get_articles():
    return list(Article.select().limit(10).order_by(Article.id.desc()).dicts())


@article_bp.route('/articles/<id>')
def get_article(id):
    article = Article.get_by_id(id)
    comments = list(Comment.select().where(Comment.article_id == id).dicts())
    return {'name': article.name, 'content': article.content, 'comments': comments}


@article_bp.route('/articles', methods=['POST'])
def add_article():
    article = Article.create(name=request.json['name'], content=request.json['content'])
    return {'id': article.id}


@article_bp.route('/articles/<id>', methods=['PUT'])
def update_article(id):
    try:
        article = Article.get_by_id(id)
        name = request.json['name']
        content = request.json['content']
        article.name = name
        article.content = content
        article.save()
        return Response(status=204)

    except Article.DoesNotExist:
        return {"error": "not found"}, 404


@article_bp.route('/articles/<id>', methods=['DELETE'])
def delete_article(id):
    try:
        article = Article.get(Article.id == id)
        article.delete_instance()
        return Response(status=204)

    except Article.DoesNotExist:
        return {"error": "not found"}, 404