FROM python:3.11.2
MAINTAINER THR Consulting <it@makingyourmilescount.com>

RUN mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -yq nano poppler-utils tesseract-ocr git

RUN mkdir -p /app
RUN mkdir -p /models

WORKDIR /app

RUN git clone https://github.com/thr-consulting/document-automation.git

# Install your Python packages
RUN pip install -r /app/document-automation/requirements.txt
RUN pip install torch torchvision --index-url https://download.pytorch.org/whl/cpu

WORKDIR /app/document-automation/src

# Run queue
CMD ["python", "-u", "/app/document-automation/src/worker.py"]