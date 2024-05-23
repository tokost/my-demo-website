# Use an Alpine-based Python image
FROM python:3.8-alpine

# Create a non-root user and group
RUN addgroup -S mygroup && adduser -S myuser -G mygroup

# Set working directory
RUN mkdir /code
WORKDIR /code

# Install system dependencies and keep them for the entire build process
RUN apk update && \
    apk add --no-cache \
    gcc \
    python3-dev \
    musl-dev \
    postgresql-dev \
    libffi-dev \
    openssl-dev \
    build-base

# Copy requirements file and install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /code/

# Set permissions for the non-root user
RUN chown -R myuser:mygroup /code

# Switch to non-root user to run the application
USER myuser

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the application
CMD ["sh", "-c", "gunicorn mywebsite.wsgi:application --bind 0.0.0.0:8000"]

