from sqlalchemy import create_engine 
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base 

# PostgreSQL connection URL: username, password, host, port, database name.
DATABASE_URL = "postgresql://postgres:mypassword@db:5432/library_api"

# Create PostgreQSL database engine
engine = create_engine(DATABASE_URL)

# Configure the session factory used to create database sessions.
SessionLocal = sessionmaker(
    autocommit=False,
    autoflush=False,
    bind=engine
)

# Base class inherited by all SQLAlchemy ORM models.
Base = declarative_base() 

# Provides a database session to FastAPI dependencies.
def get_db():
    db = SessionLocal()
    try: 
        yield db
    finally: 
        # Always close the session after the request is completed.
        db.close()


