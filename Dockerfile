# Use an official Python runtime as the base image.
FROM python:3.12-slim

# Set the working directory inside the container.
WORKDIR /app

# Install Python dependencies.
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code.
COPY app ./app

# Copy Alembic configuration and migration files.
COPY alembic.ini .
COPY alembic ./alembic

# Start the application.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
