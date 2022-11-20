from classes import *


# GENRES
def add_genre(name: str):
    """
    Add new genre to the database
    :param name: genre name
    """
    new_genre = Genre.create(genre_name=name)


def get_genre_id(name: str) -> int:
    """
    Get genres id
    :param name: name of genre
    :return: genre id
    """
    genre = Genre.get(Genre.genre_name == name)
    return genre.genre_id


def all_genres() -> list[str]:
    """
    List with all genres possible
    :return: list of strings
    """
    query = Genre.select()
    return [genre.genre_name for genre in query]


# AUTHORS
def add_author(name: str):
    """
    Add author to the database
    :param name: author's name
    """
    new_auth = Author.create(author_name=name)


def get_author_id(name: str) -> int:
    """
    Find authors id by their name
    :param name: author's name
    :return: author id
    """
    author = Author.get(Author.author_name == name)
    return author.author_id


def all_authors() -> list[str]:
    """
    List with all authors possible
    :return: list of authors
    """
    query = Author.select()
    return [author.author_name for author in query]


# BOOKS
def add_book(name: str, author: str, genre: str, bookshelf: str, shelf: str):
    """
    Add book to the shelf
    :param name: name of the book
    :param author: the author
    :param genre: genre of the book
    :param bookshelf: bookshelf name
    :param shelf: shelf name
    """
    # если книга есть - обновлять данные
    genre_id = get_genre_id(genre)
    shelf_id = get_storage_id(bookshelf, shelf)
    new_book = Book(book_name=name, book_genre=genre_id, book_stor=shelf_id)
    new_book.save()
    add_relation(name, author)


def test_data(author1: str, author2: str, genre1: str, genre2: str) -> (str, str):
    """
    Testing input data and sending the right one
    :param author1: author from combo box
    :param author2: author from edit line
    :param genre1: genre from combo box
    :param genre2: genre from edit line
    """
    if not author2 and not genre2:
        return author1, genre1
    if author2 and not genre2:
        if author2 not in all_authors():
            add_author(author2)
        return author2, genre1
    if genre2 and not author2:
        if genre2 not in all_genres():
            add_genre(genre2)
        return author1, genre2
    if author2 and genre2:
        if author2 not in all_authors():
            add_author(author2)
        if genre2 not in all_genres():
            add_genre(genre2)
        return author2, genre2



def get_book_id(name: str) -> int:
    """
    Get book ID by its name
    :param name: name of the book
    :return: book id
    """
    book = Book.get(Book.book_name == name)
    return book.book_id


def get_book_author(name: str) -> str:
    """
    Get book's author by it's name
    :param name: name of the book
    :return: author
    """
    book_id = get_book_id(name)
    rel = Relation.get(Relation.book_id == book_id)
    author_id = rel.author_id
    return author_id


def get_book_position(book_id: int) -> int:
    """
    Find book by its id
    :param book_id: ID of the book
    :return: unique shelf id
    """
    book = Book.get(Book.book_id == book_id)
    return book.book_stor


def delete_book(book_name:str, shelf_id:int):
    """
    Delete book
    :param book_name: book's name
    :param shelf_id: shelf ID
    """
    book = Book.get((Book.book_name == book_name) & (Book.book_stor == shelf_id))
    book.delete_instance()

def all_books_on_shelf(location: int) -> list[str]:
    """
    Return list with all books
    :param location: bookshelf ID
    :return: list
    """
    query = Book.select().where(Book.book_stor == location)
    return [book.book_name for book in query]


# RELATIONS
def add_relation(book: str, author: str):
    """
    Add new relation of book and its author
    :param book: book name
    :param author: author name
    """
    book_id = get_book_id(book)
    author_id = get_author_id(author)
    new_relation = Relation(book_id=book_id, author_id=author_id)
    new_relation.save()


# STORAGE
def add_bookshelf(name: str, n: int):
    """
    Add a bookshelf with n shelves
    :param name: name of the bookshelf
    :param n: Int, Number of shelves
    """
    new_homeshelf = Storage(storage_name=name)
    new_homeshelf.save()
    for i in range(n):
        new_shelf = Storage(storage_name='Полка '+str(i+1), storage_link=new_homeshelf)
        new_shelf.save()


def get_storage_id(bs_name: str, s_name:str=None) -> int:
    """
    Get storage ID by its name
    :param bs_name:
    :param s_name: name of
    :return: storage ID
    """
    bs = Storage.get((Storage.storage_name == bs_name) & (Storage.storage_link == None))
    if s_name:
        s = Storage.get((Storage.storage_name == s_name) & (Storage.storage_link == bs.storage_id))
        return s.storage_id
    else:
        return bs.storage_id

def delete_storage(bs_name: str, s_name:str=None):
    """
    Delete bookshelf or shelf
    :param bs_name: name of bookshelf
    :param s_name: name of shelf
    :return:
    """
    if not s_name:
        bs_id = get_storage_id(bs_name)
        Storage.delete_by_id(bs_id)
    else:
        s_id = get_storage_id(bs_name, s_name)
        Storage.delete_by_id(s_id)


def all_bookshelves() -> list[str]:
    """
    Return all bookshelves
    :return: list of names
    """
    query = Storage.select().where(Storage.storage_link == None)
    return [storage.storage_name for storage in query]


def all_shelves(id: int) -> list[str]:
    """
    Return all shelves in a bookshelf
    :param id: bookshelf ID
    :return: list of names
    """
    query = Storage.select().where(Storage.storage_link == id)
    return [storage.storage_name for storage in query]


#VIEW
def all_cabinets():
    Shelf = Storage.alias()
    all_storage = (Storage.select(Storage.storage_name, Shelf.storage_id, Shelf.storage_name.alias('shelf_name'))
    .join(Shelf, on=(Storage.storage_id == Shelf.storage_link), attr='shelf')
    .where(Storage.storage_link==None))

    res = []

    for storages in all_storage:
        res.append([storages.storage_name, storages.shelf.shelf_name, '', '', ''])
        all_book = (
            Book.select(Book.book_id, Book.book_name, Genre.genre_name, Author.author_name)
            .join(Genre, on=(Book.book_genre == Genre.genre_id), attr='genre')
            .switch(Book)
            .join(Relation, on=(Relation.book_id == Book.book_id), attr='relation')
            .join(Author, on=(Author.author_id == Relation.author_id), attr='author')
            .where(Book.book_stor == storages.shelf.storage_id)
        )
        for books in all_book:
            res.append(['', '', books.book_name, books.relation.author.author_name, books.genre.genre_name])
    return res
