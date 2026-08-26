from fastapi import FastAPI

from .routers import books 

# Initialize the FastAPI application. 
app = FastAPI() 

# Register book-related endpoints.
app.include_router(books.router)