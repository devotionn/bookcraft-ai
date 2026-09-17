import pytest

from bookcraft.models import Book, Chapter


def test_book_requires_title():
    book = Book(title="   ")
    with pytest.raises(ValueError, match="book title is required"):
        book.validate()


def test_chapter_ids_must_be_unique():
    book = Book(
        title="Demo",
        chapters=[Chapter(id="ch-1", title="One"), Chapter(id="ch-1", title="Two")],
    )
    with pytest.raises(ValueError, match="chapter ids must be unique"):
        book.validate()


def test_valid_book_passes():
    book = Book(
        title="Demo",
        chapters=[Chapter(id="ch-1", title="One"), Chapter(id="ch-2", title="Two")],
    )
    book.validate()
    assert book.chapter_ids() == ["ch-1", "ch-2"]
