#!/bin/bash

set -o errexit

# Upgrade pip and install certificates
python3 -m pip install --upgrade pip
python3 -m pip install certifi pymongo[srv]

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate --noinput

