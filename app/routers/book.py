from datetime import datetime, timezone

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session

from ..database import get_db
from ..models.book import Book
from ..schemas.book import BookCreate, BookResponse, BorrowBook

# Creates router for endpoints related to the library's books.
# Shares exact same settings for those endpoints.
router = APIRouter(prefix="/books", tags=["books"])


@router.post("/", response_model=BookResponse)
def create_book(book_data: BookCreate, db: Session = Depends(get_db)):
    """
    Creates a new book.

    Args:
        book_data: Validated book data containing the serial number, title,
            and author.
        db: Database session used to persist the book.
    """

    # Creates a new book from the validated request data.
    book = Book(
        serial_number=book_data.serial_number,
        title=book_data.title,
        author=book_data.author,
    )

    # Add the book to the current database transaction.
    db.add(book)

    # Commit the transaction.
    db.commit()

    # Refresh the object to reflect the current database state.
    db.refresh(book)

    return book


@router.patch("/{serial_number}/borrow")
def borrow_book(
    serial_number: int, borrow_data: BorrowBook, db: Session = Depends(get_db)
):
    """
    Updates borrowed book's state.

    Args:
        serial_number: Unique six-digit identifier assigned to the book.
        borrow_data: Request schema for borrowing a book.
        db: Database session used to persist the book.
    """

    # Query the book by its serial number.
    book = db.query(Book).filter(Book.serial_number == serial_number).first()

    # Error handling.
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    if book.is_borrowed:
        raise HTTPException(status_code=409, detail="Book is already borrowed")

    # Update book parameters.
    book.is_borrowed = True
    book.borrowed_at = datetime.now(timezone.utc)
    book.user_card_number = borrow_data.user_card_number

    # Commit the transaction.
    db.commit()

    # Refresh the object to reflect the current database state.
    db.refresh(book)

    return book


@router.patch("/{serial_number}/return", response_model=BookResponse)
def return_book(serial_number: int, db: Session = Depends(get_db)):
    """
    Returns a borrowed book to the library.

    Args:
        serial_number: Unique identifier assigned to the book.
        db: Database session used to persist the book.
    """

    # Query the book by its serial number.
    book = db.query(Book).filter(Book.serial_number == serial_number).first()

    # Error handling.
    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    # Check whether the book is currently borrowed.
    if not book.is_borrowed:
        raise HTTPException(status_code=400, detail="Book is not currently borrowed")

    # Reset the book's borrowed state.
    book.is_borrowed = False
    book.borrowed_at = None
    book.user_card_number = None

    # Commit the transaction.
    db.commit()

    # Refresh the object to reflect the current database state.
    db.refresh(book)

    return book


@router.get("/", response_model=list[BookResponse])
def get_book_list(db: Session = Depends(get_db)):
    """
    Gets a list of all books from the library.

    Args:
        db: Database session to get the list of books.
    """

    # Query all books from the database
    books = db.query(Book).all()
    return books


@router.delete("/{serial_number}")
def delete_book(serial_number: int, db: Session = Depends(get_db)):

    book = db.query(Book).filter(Book.serial_number == serial_number).first()

    if book is None:
        raise HTTPException(status_code=404, detail="Book not found")

    db.delete(book)
    db.commit()

    return {"message": "Book deleted successfully"}
