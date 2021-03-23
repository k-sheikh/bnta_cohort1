from flask import Flask, render_template, flash, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from forms import NewAuthorForm
from api import api

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/books_and_authors.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'put some random string here'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'

app.register_blueprint(api, url_prefix='/api')

db = SQLAlchemy(app)

migrate = Migrate(app, db)

from models import Author, Book

admin = Admin(app, name='Books and Authors', template_mode='bootstrap3')
admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(Book, db.session))


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/books')
def list_books():
    books_by_author = {
        author: Book.query.filter(Book.author == author)
        for author in Author.query.all()
    }
    return render_template('books.html', authors=Author.query.all(), books_by_author=books_by_author)


@app.route('/new_author', methods=['GET', 'POST'])
def new_author():
    form = NewAuthorForm()
    if not form.validate_on_submit():
        return render_template('new_author.html', form=form)

    name = form.name.data.strip()
    year_of_birth = int(form.year_of_birth.data)

    if Author.query.filter(Author.name == name).count():
        flash(f'Error: {name} already exists')
        return render_template('new_author.html', form=form)

    author = Author(name=name, year_of_birth=year_of_birth)
    db.session.add(author)
    db.session.commit()
    flash(f'New author {name} created')
    return redirect('/books')
