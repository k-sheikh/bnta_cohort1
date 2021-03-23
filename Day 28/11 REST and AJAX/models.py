from app import db

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
