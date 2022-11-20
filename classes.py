from peewee import *


db = SqliteDatabase("/home/sonya/Downloads/SQLiteStudio/books_cabinet.sqlite")


class Base(Model):
    class Meta:
        database = db


class Storage(Base):
    storage_id = AutoField()
    storage_name = TextField(unique=True)
    storage_link = ForeignKeyField(column_name='storage_link', field='storage_id', model='self')


class Author(Base):
    author_id = IntegerField(primary_key=True)
    author_name = TextField(unique=True)


class Genre(Base):
    genre_id = IntegerField(primary_key=True, unique=True)
    genre_name = TextField(unique=True)


class Book(Base):
    book_id = IntegerField(primary_key=True, unique=True)
    book_name = TextField()
    book_genre = ForeignKeyField(Genre, column_name='book_genre')
    book_stor = ForeignKeyField(Storage, column_name='book_stor')


class Relation(Base):
    book_id = ForeignKeyField(Book, column_name='book_id')
    author_id = ForeignKeyField(Author, column_name='author_id')
