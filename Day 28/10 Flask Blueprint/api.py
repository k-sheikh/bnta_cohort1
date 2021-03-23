from flask import Blueprint, request

api = Blueprint('api', __name__)


@api.route('/book')
def books_for_author():
    author_id = request.args.get('author_id')
    return f'List of books for author {author_id} here please'
