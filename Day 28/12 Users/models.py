from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

from app import db
from app import login


class Author(db.Model):
    __tablename__ = 'author'
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String)
    year_of_birth = db.Column(db.Integer)

    def __repr__(self):
        return f'{self.name} ({self.year_of_birth})'


class Book(db.Model):
    __tablename__ = 'book'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    year_of_publication = db.Column(db.Integer)
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship(Author)
    copies_sold = db.Column(db.Integer, default=0)

    def __repr__(self):
        return f'{self.title} by {self.author.name}'

    def as_dict(self):
        return dict(
            id=self.id,
            title=self.title,
            year_of_publication=self.year_of_publication,
            author_id=self.author_id,
            copies_sold=self.copies_sold if self.copies_sold else 0
        )


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))
