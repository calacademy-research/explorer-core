# Use an official Python runtime as a parent image
FROM python:3.10

#Install Nginx and supervisor
RUN apt-get update && apt-get install -y nginx netcat-openbsd && apt-get install iputils-ping && rm -rf /var/lib/apt/lists/*

# Set the working directory in the container
WORKDIR /collections_app

# Copy project files
#COPY . /app/
COPY . .

COPY nginx/supervisord.conf /etc/supervisor/conf.d/supervisord.conf
COPY nginx/nginx.conf /etc/nginx/nginx.conf
# Create log directory
RUN mkdir -p /var/log/supervisor

RUN python -m venv /venv

ENV PATH="/venv/bin:$PATH"

# Install Python dependencies using pip within the virtual environment
RUN /venv/bin/pip install --no-cache-dir -r requirements.txt

# Explicitly install Gunicorn (if not included in requirements.txt)
#RUN /venv/bin/pip install gunicorn

# Verify Gunicorn installation (for debugging)
RUN /venv/bin/gunicorn --version || echo "Gunicorn not installed correctly"

# Copy the wait-for-it script
COPY wait-for-it.sh /wait-for-it.sh
RUN chmod +x /wait-for-it.sh

# Collect static files
#RUN python manage.py collectstatic --noinput
#RUN pip install gunicorn

RUN python manage.py collectstatic --noinput

EXPOSE 8001

# Define the command to run your application
CMD ["gunicorn", "explorer-core.wsgi:application", "--bind", "0.0.0.0:8000"]

# Set the default command to use Gunicorn to run the app
 #CMD ["gunicorn", "explorer-core.wsgi:application", "--bind", "0.0.0.0:8001"]
