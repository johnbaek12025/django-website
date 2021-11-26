FROM python:3.10-slim as production


WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY manage.py manage.py
COPY hackershack_website hackershack_website

EXPOSE 8000