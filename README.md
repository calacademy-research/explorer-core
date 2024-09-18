# explorer-core
Docker compose of collections explorer core (Django API container, mySQL container, nginx container)
Nginx depends on Django web, Django web relies on mySQL


Docker Compose version v2.26.1-desktop.1

Docker Engine - Community version 27.2.0



$ _docker compose up --build_



Things to modify before build:
-
.env
- add .env file to root of Django project folder (explorer-core/.env)
- add your machine's IP address to the DJANGO_ALLOWED_HOSTS list variable in .env


nginx.conf
- change server_name variable value to your IP address

collections_app_api/static/
- create a static folder in "collections_app_api" add the static files of the 3D scans 
