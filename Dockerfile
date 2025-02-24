FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

ENV PYTHONUNBUFFERED=1
ENV PORT=10000
ENV DEBUG=False
ENV DJANGO_SETTINGS_MODULE=config.settings

EXPOSE 10000

CMD ["sh", "-c", "python manage.py migrate && gunicorn config.wsgi:application --bind 0.0.0.0:$PORT --workers 4 --timeout 120 --log-level debug"]

