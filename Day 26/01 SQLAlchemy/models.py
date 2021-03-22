from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

Base = declarative_base()


class Author(Base):
    __tablename__ = 'author'
    id = Column(Integer, primary_key=True)
    name = Column(String)
    year_of_birth = Column(Integer)


class Book(Base):
    __tablename__ = 'book'
    id = Column(Integer, primary_key=True)
    title = Column(String)
    year_of_publication = Column(Integer)
    author_id = Column(Integer, ForeignKey('author.id'))
    author = relationship(Author)


engine = create_engine('sqlite:///../data/books_and_authors.sqlite')

session = sessionmaker()
session.configure(bind=engine)
