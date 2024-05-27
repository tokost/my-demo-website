# Use an Alpine-based Python image
FROM python:3.8-alpine3.18

# Create a non-root user and group
RUN addgroup -S mygroup && adduser -S myuser -G mygroup

# Set working directory
RUN mkdir /code
WORKDIR /code

# Install system dependencies and keep them for the entire build process
RUN apk update --repository=http://dl-cdn.alpinelinux.org/alpine/edge/main && \
    apk add --no-cache gcc && \
    apk add --no-cache python3-dev && \
    apk add --no-cache musl-dev && \
    apk add --no-cache postgresql-dev && \
    apk add --no-cache libffi-dev && \
    apk add --no-cache openssl-dev && \
    apk add --no-cache build-base

# Copy requirements file and install Python dependencies
COPY requirements.txt /code/
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . /code/

# Set permissions for the non-root user
RUN chown -R myuser:mygroup /code
RUN chmod -R 755 /code

# Switch to non-root user to run the application
USER myuser

# Make port available to the world outside this container
EXPOSE 8000

# Define environment variable
ENV NAME World

# Run the application
CMD ["sh", "-c", "gunicorn mywebsite.wsgi:application --bind 0.0.0.0:8000"]

