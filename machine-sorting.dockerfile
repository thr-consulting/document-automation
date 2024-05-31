FROM python:3.10
MAINTAINER THR Consulting <it@makingyourmilescount.com>

RUN mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -yq nano poppler-utils tesseract-ocr

RUN mkdir -p /app
RUN mkdir -p /models

WORKDIR /app

# Copy your Python packages
COPY requirements.txt /app/requirements.txt

# Install your Python packages
RUN pip install -r /app/requirements.txt

# Copy your application code
COPY . /app

# Run queue
CMD ["python", "worker.py"]