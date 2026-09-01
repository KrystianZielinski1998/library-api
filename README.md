# library-api

# **library-api**   
 **A REST API for managing books in a library.**  

---

## ** Overview**  

Library API is a backend REST API for managing books in a library.

The API allows users to:

- Add new books to the library
- View all available books
- Borrow books using a library card number
- Return borrowed books
- Delete books from the library
- Prevent books from being borrowed while they are already borrowed
- Validate six-digit book serial numbers and library card numbers

The application uses FastAPI for the API layer, SQLAlchemy for database interaction, PostgreSQL for data storage, and Alembic for database migrations.

The entire application can be run using Docker Compose, which starts both the FastAPI application and PostgreSQL database.

The project also uses GitHub Actions and Ruff for automated code quality checks.

## ** Tech Stack **

- **Python 3.12** - Programming language
- **FastAPI** - Web framework for building the REST API
- **Uvicorn** - ASGI server used to run the FastAPI application
- **SQLAlchemy** - ORM for database interaction
- **PostgreSQL 17** - Relational database
- **Alembic** - Database migration management
- **psycopg2** - PostgreSQL database adapter for Python
- **Docker** - Containerization and service orchestration
- **GitHub Actions & Ruff** - Code formatting and linting

## ** Project structure**  

```text
library-api/
├── .github/
│   └── workflows/
│       └── lint.yml                  # GitHub Actions workflow for code quality checks
│
├── alembic/
│   ├── versions/                    # Database migration files
│   ├── env.py                       # Alembic environment and SQLAlchemy configuration
│   └── script.py.mako               # Template used to generate migration files
│
├── app/
│   ├── models/
│   │   ├── __init__.py              # Makes models available as a Python package
│   │   └── book.py                  # SQLAlchemy Book database model
│   │
│   ├── routers/
│   │   └── book.py                  # API endpoints for book operations
│   │
│   ├── schemas/
│   │   └── book.py                  # Pydantic schemas for request/response validation
│   │
│   ├── database.py                  # Database engine, sessions and SQLAlchemy Base
│   └── main.py                      # FastAPI application entry point
│
├── alembic.ini                      # Alembic configuration
├── Dockerfile                       # Docker image configuration for the API
├── docker-compose.yml               # Defines and runs the API and PostgreSQL services
├── requirements.txt                 # Python project dependencies
└── README.md                        # Project documentation
```



## ** Start the application**  


