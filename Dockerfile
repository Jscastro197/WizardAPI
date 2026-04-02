# Start with an official Python image
FROM python:3.14.3

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Create a working directory for the app
WORKDIR /app

# Copy the requirements file and install dependencies
COPY pyproject.toml .
RUN pip install --no-cache-dir .

# Copy the app source code
COPY . /app

# Expose the port FastAPI will run on
EXPOSE 8000

# Start FastAPI using Uvicorn
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]