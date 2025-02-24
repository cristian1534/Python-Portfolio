#!/bin/bash

set -o errexit

# Upgrade pip
python3 -m pip install --upgrade pip

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate --noinput

