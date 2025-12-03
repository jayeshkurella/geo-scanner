# Use official Python image
FROM python:3.10-slim

# Set working directory in container
WORKDIR /app

# Install required system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    libpq-dev \
    build-essential \
    python3-dev \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Upgrade pip and install dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project
COPY . .

# Expose the port Django runs on
EXPOSE 3333

# Run the app
CMD ["python", "manage.py", "runserver", "0.0.0.0:3002"]
