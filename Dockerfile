FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

ENV PORT=8000

CMD ["gunicorn", "--config", "gunicorn.conf.py", "config.wsgi:application"]