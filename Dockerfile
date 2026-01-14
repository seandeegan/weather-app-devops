# 1. Use an official Python base image (a tiny version of Linux with Python)
FROM python:3.9-slim

# 2. Set the working directory inside the container
WORKDIR /app

# 3. Install the "Flask" library (needed for our app)
RUN pip install flask

# 4. Copy your app.py file from your computer into the container
COPY app.py .

# 5. Tell the container to listen on port 5000
EXPOSE 5000

# 6. The command to run your app when the container starts
CMD ["python", "app.py"]
