FROM python:3.10.0a3-buster

# Make a directory for our application
WORKDIR /application

# install dependencies
RUN pip install requests

# Copy source code
COPY /application .

# Run the application
CMD ["python","app.py"]