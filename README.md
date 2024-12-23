# BooksCollector Tests

This repository contains tests for the `BooksCollector` class, which allows adding books, setting their genres, and managing a list of favorite books.

## Tests Implemented

1. **test_add_new_book**: Tests adding a new book to the `books_genre` dictionary.
2. **test_set_book_genre**: Tests setting the genre of a book.
3. **test_get_book_genre**: Tests retrieving the genre of a book.
4. **test_get_books_with_specific_genre**: Tests retrieving a list of books with a specific genre.
5. **test_get_books_genre**: Tests retrieving the current `books_genre` dictionary.
6. **test_get_books_for_children**: Tests retrieving books suitable for children.
7. **test_add_book_in_favorites**: Tests adding a book to the favorites list.
8. **test_delete_book_from_favorites**: Tests removing a book from the favorites list.
9. **test_get_list_of_favorites_books**: Tests retrieving the list of favorite books.
10. **test_add_new_book_parametrized**: Parameterized test for adding books with different name lengths.

## Running the Tests

To run the tests, use the following command:

```sh
pytest -v tests.py
