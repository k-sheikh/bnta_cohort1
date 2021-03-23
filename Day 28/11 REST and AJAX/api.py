import sqlalchemy.orm
from flask import Blueprint, request, abort, jsonify

from models import Author, Book

api = Blueprint('api', __name__)


@api.route('/book')
def books_for_author():
    try:
        author_id = int(request.args.get('author_id'))
        author = Author.query.filter(Author.id == author_id).one()
    except ValueError:
        # author_id not a number
        abort(404)
    except sqlalchemy.orm.exc.NoResultFound:
        # No author found for this id
        abort(404)

    books = Book.query.filter(Book.author_id == author_id).all()
    return jsonify([book.as_dict() for book in books])
