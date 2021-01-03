FROM python:3

WORKDIR /usr/src/app

# install dependencies
RUN pip install requests

# Copy source code
COPY . /usr/src/app

# Run the application
CMD ["python","app.py"]