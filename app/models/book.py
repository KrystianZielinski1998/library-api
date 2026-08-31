from sqlalchemy import Boolean, Column, DateTime, Integer, String 
from ..database import Base

class Book(Base):
    """ Represents the current state of a library book. """

    # Defines name of the table in database.
    __tablename__ = "books"

    # Unique serial number of a book.
    serial_number = Column(Integer, primary_key=True)

    # Book's title.
    title = Column(String, nullable=False)

    # Book's author.
    author = Column(String, nullable=False)

    # Book's state - either borrowed or available. 
    is_borrowed = Column(Boolean, default=False)

    # Date of when book was borrowed.
    borrowed_at = Column(DateTime, nullable=True)

    # Card number of a user who borrowed a book.
    user_card_number = Column(Integer, nullable=True)

