import os

try:
    port = int(os.environ.get('PORT', 8000))
except ValueError:
    port = 8000

bind = f'0.0.0.0:{port}'
workers = 4
timeout = 120