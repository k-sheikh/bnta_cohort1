from flask import Flask, render_template, flash, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView
from flask_login import LoginManager, current_user, login_user, logout_user, login_required

from forms import NewAuthorForm, NewUserForm, LoginForm

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///../data/books_and_authors.sqlite'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'put some random string here'
app.config['FLASK_ADMIN_SWATCH'] = 'cerulean'


db = SQLAlchemy(app)

migrate = Migrate(app, db)
login = LoginManager(app)
login.login_view = 'login'

from models import Author, Book, User
from api import api
app.register_blueprint(api, url_prefix='/api')

admin = Admin(app, name='Books and Authors', template_mode='bootstrap3')
admin.add_view(ModelView(Author, db.session))
admin.add_view(ModelView(Book, db.session))
admin.add_view(ModelView(User, db.session))


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


@app.route('/books_for_author')
@login_required
def books_for_author():
    return render_template('books_for_author.html', authors=Author.query.all())


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if not form.validate_on_submit():
        return render_template('login.html', form=form)

    user = User.query.filter_by(username=form.username.data).first()
    if user is None or not user.check_password(form.password.data):
        flash('Invalid username or password')
        return redirect(url_for('login'))

    login_user(user)
    return redirect(url_for('index'))


@app.route('/register', methods=['GET', 'POST'])
def new_user():
    form = NewUserForm()
    if not form.validate_on_submit():
        return render_template('new_user.html', form=form)

    user = User(username=form.username.data)
    user.set_password(form.password.data)
    db.session.add(user)
    db.session.commit()
    flash(f'New user {form.username.data} registered')
    return redirect(url_for('login'))


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('index'))
