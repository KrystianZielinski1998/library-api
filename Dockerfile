# Use an official Python runtime as the base image.
FROM python:3.12-slim

# Set the working directory inside the container.
WORKDIR /app

# Copy the dependency file into the container.
COPY requirements.txt .

# Install Python dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application source code into the container.
COPY app/ ./app/

# Start the FastAPI application.
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]

