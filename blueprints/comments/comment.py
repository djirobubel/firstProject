from flask import Blueprint, request, Response
from models import *

comment_bp = Blueprint('comment', __name__)


@comment_bp.route('/comments')
def get_comments():
    return list(Comment.select().dicts())


@comment_bp.route('/comments/<article_id>', methods=['POST'])
def add_comment(article_id):
    comment = Comment.create(content=request.json['content'], article_id=article_id)
    return {'id': comment.id}


@comment_bp.route('/comments/<id>', methods=['PUT'])
def update_comment(id):
    try:
        comment = Comment.get_by_id(id)
        content = request.json['content']
        comment.content = content
        comment.save()
        return Response(status=204)

    except Comment.DoesNotExist:
        return {"error": "not found"}, 404


@comment_bp.route('/comments/<id>', methods=['DELETE'])
def delete_comment(id):
    try:
        comment = Comment.get(Comment.id == id)
        comment.delete_instance()
        return Response(status=204)

    except Comment.DoesNotExist:
        return {"error": "not found"}, 404