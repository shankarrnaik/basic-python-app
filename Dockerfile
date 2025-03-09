# Dockerfile
FROM python:3.8-slim

WORKDIR /app

# Copy and install dependencies (if any)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY . .

# Expose port if your app listens on a port (optional)
# EXPOSE 5000

# Command to run the application
CMD ["python", "app.py"]
