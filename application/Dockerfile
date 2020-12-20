FROM python:3-onbuild

# install dependencies
RUN pip install requests

# Copy source code
COPY . /usr/src/app

# Run the application
CMD ["python","app.py"]