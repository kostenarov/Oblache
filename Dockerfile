FROM python:3.9-slim-buster

# Set working directory
WORKDIR /app

# Copy requirements file
COPY requirements.txt .

# Install dependencies
RUN pip3 install --no-cache-dir -r requirements.txt

# Copy server and client code
COPY server.py .
COPY client.py .

# Expose port 12345 for the server
EXPOSE 12345

# Start the server by default
CMD ["python3", "server.py"]