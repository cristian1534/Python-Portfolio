#!/bin/bash

set -o errexit

# Upgrade pip and install certificates
python3 -m pip install --upgrade pip
python3 -m pip install certifi==2025.1.31
python3 -m pip install "pymongo[srv]>=3.12.3"
python3 -m pip install "dnspython>=2.7.0"

# Install dependencies
python3 -m pip install -r requirements.txt

# Collect static files
python3 manage.py collectstatic --noinput --clear

# Run migrations
python3 manage.py makemigrations
python3 manage.py migrate --noinput

