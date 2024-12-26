# Use the official Python image from the Docker Hub.
FROM python:3.12-slim

# Set environment variables to prevent Python from writing pyc files and to ensure output is flushed.
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set the working directory inside the container.
WORKDIR /app

# Copy the requirements file into the container.
COPY requirements.txt .

# Install dependencies.
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container.
COPY . .

# Expose port 8000 for the Django application.
EXPOSE 8000

# Command to run the Django development server.
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
