# Use an official Python runtime as a parent image
FROM python:3.10-alpine

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements.txt file to the working directory
COPY requirements.txt requirements.txt

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project directory to the working directory
COPY . .

# Expose the Flask port
EXPOSE 5001

# Set the command to run the Flask application
CMD ["flask", "run", "--host=0.0.0.0", "--port=5001"]
