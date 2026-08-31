from fastapi import FastAPI

from .routers import book

# Initialize the FastAPI application. 
app = FastAPI() 

# Register book-related endpoints.
app.include_router(book.router)