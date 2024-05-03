FROM python:3.10

RUN mkdir -p /usr/share/man/man1 && \
    apt-get update && \
    apt-get install -yq nano poppler-utils tesseract-ocr

WORKDIR /app

# Copy your Python packages
COPY requirements.txt /app/requirements.txt

# Install your Python packages
RUN pip install -r /app/requirements.txt

# Copy your application code
COPY . /app

# Run api
# CMD ["uvicorn", "api:app", "--host", "0.0.0.0", "--port", "80"]

# Run queue
CMD ["python", "workerBullMq.py"]