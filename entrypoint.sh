#!/bin/bash
#set -e

# Wait for mysql container to be ready
echo "Waiting for MySQL to be ready..."
until nc -z -v -w30 $DB_HOST $DB_PORT; do
  echo "Waiting for MySQL connection..."
  sleep 5
done

# Collect static files"
echo "Collecting static files...."
source /.venv/bin/activate

python manage.py collectstatic --noinput
# Run migrations (including makemigrations if necessary)
echo "Running migrations......."
python manage.py makemigrations --noinput
python manage.py migrate --noinput

# Start the Django application4701d95f5433
echo "Starting collections_app_api...."
#exec "$@"
exec gunicorn explorer-core.wsgi:application --bind 0.0.0.0:8001