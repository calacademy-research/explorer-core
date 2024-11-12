#!/bin/bash
set -e

# Collect static files
python manage.py collectstatic --noinput

# Start the Django application
exec "$@"
