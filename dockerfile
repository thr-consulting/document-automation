FROM python:3.11.2
LABEL THR Consulting <it@makingyourmilescount.com>

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
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

# Copy your application code
COPY . /app

# Run queue
CMD ["python", "./src/worker.py"]