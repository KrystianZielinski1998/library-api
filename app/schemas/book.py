from pydantic import BaseModel, Field
from datetime import datetime 


class BookCreate(BaseModel):
    """ Request schema for adding a new book. """

    # Unique six-digit identifier assigned to the book.
    serial_number: int = Field(
        ge=100000,
        le=999999
    )

    # Book information provided when creating the record.
    title: str 
    author: str 

class BorrowBook(BaseModel):
    """ Request schema for borrowing a book. """

    # Six-digit library card number of the borrower.
    user_card_number: int = Field(
        ge=100000,
        le=999999
    )

class BookResponse(BaseModel):
    """ Response schema representing the current state of a book. """

    serial_number: int
    title: str
    author: str
    is_borrowed: bool

    # Empty when the book is currently available.
    borrowed_at: datetime | None

    # Empty when the book is currently available.
    user_card_number: int | None

    # Allow Pydantic to build the response model from SQLAlchemy model attributes.
    model_config = {"from_attributes": True}


