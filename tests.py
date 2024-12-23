import pytest
from main import BooksCollector
def test_add_new_book():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    assert collector.books_genre['Книга 1'] == ''
    assert len(collector.books_genre) == 1
@pytest.mark.parametrize("name, genre", [
    ('Книга 1', 'Фантастика'),
    ('Книга 2', 'Ужасы'),
    ('Книга 3', 'Детективы')
])
def test_set_book_genre(name, genre):
    collector = BooksCollector()
    collector.add_new_book(name)
    collector.set_book_genre(name, genre)
    assert collector.books_genre[name] == genre
def test_get_book_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Фантастика')
    assert collector.get_book_genre('Книга 1') == 'Фантастика'
@pytest.mark.parametrize("genre, expected", [
    ('Фантастика', ['Книга 1']),
    ('Ужасы', ['Книга 2'])
])
def test_get_books_with_specific_genre(genre, expected):
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.set_book_genre('Книга 2', 'Ужасы')
    assert collector.get_books_with_specific_genre(genre) == expected
def test_get_books_genre():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.set_book_genre('Книга 1', 'Фантастика')
    assert collector.get_books_genre() == {'Книга 1': 'Фантастика'}
def test_get_books_for_children():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_new_book('Книга 2')
    collector.set_book_genre('Книга 1', 'Фантастика')
    collector.set_book_genre('Книга 2', 'Ужасы')
    assert collector.get_books_for_children() == ['Книга 1']
def test_add_book_in_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_book_in_favorites('Книга 1')
    assert collector.favorites == ['Книга 1']
def test_delete_book_from_favorites():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_book_in_favorites('Книга 1')
    collector.delete_book_from_favorites('Книга 1')
    assert collector.favorites == []
def test_get_list_of_favorites_books():
    collector = BooksCollector()
    collector.add_new_book('Книга 1')
    collector.add_book_in_favorites('Книга 1')
    assert collector.get_list_of_favorites_books() == ['Книга 1']
@pytest.mark.parametrize("name, expected", [
    ('Книга 1', True),
    ('К' * 40, True),
    ('К' * 41, False),
    ('', False)
])
def test_add_new_book_parametrized(name, expected):
    collector = BooksCollector()
    collector.add_new_book(name)
    assert (name in collector.books_genre) == expected
