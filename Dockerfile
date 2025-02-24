FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1

EXPOSE 8000 

CMD ["sh", "-c", "gunicorn --bind 0.0.0.0:$PORT config.wsgi:application"]
