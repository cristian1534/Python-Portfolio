FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=8000
ENV DEBUG=False

EXPOSE 8000

CMD gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --timeout 120 --access-logfile - --error-logfile -

