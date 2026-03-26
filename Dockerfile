# Use a lightweight Python base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Expose port 80 (the port our Flask app is running on)
EXPOSE 80

# Command to run the application
CMD ["python", "app.py"]
# CMD ["bash", "rahul.sh"]
