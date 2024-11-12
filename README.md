# explorer-core
Docker compose of collections explorer core (Django API container, mySQL container, nginx container)
Nginx depends on Django web, Django web relies on mySQL

Docker Compose version v2.26.1-desktop.1
Docker Engine - Community version 27.2.0


>Things to modify before build:
>
>>_.env (Request from Jenna)_
>>- add .env file to root of Django project folder (explorer-core/.env)
>>- add your machine's IP address to the DJANGO_ALLOWED_HOSTS list variable in .env
>
>>_collections_app_api/static/_
>>- create a static folder in "collections_app_api" add the static files (example file _casxlogo.png_ included)

---
# Local Deployment
There is a shell script _dc_start.sh_ to make building and starting more convenient:
```bash
./dc_start.sh up
``` 

The same shell script can be used to stop and remove the Docker containers:
```bash
./dc_start.sh down
```
API runs on _0.0.0.0_ after successful deployment.

Visit _0.0.0.0/api/docs_ to view API document (_/collections_app_api/collections_schema.yaml_).

Static files served through nginx on _0.0.0.0/static/_

# GCP Deployment
 
This api is hosted as Cloud Run container on Google Cloud Platform. The project is named `galapagateway`.
After installing the gcloud cli and authenticating, you can build the docker image on remote:
```bash
gcloud builds submit --tag us-central1-docker.pkg.dev/galapagateway/cloud-run-source-deploy/api --project galapagateway .
```

Once the build is complete, update the service to run that container:
```bash
gcloud run deploy --image us-central1-docker.pkg.dev/galapagateway/cloud-run-source-deploy/api:latest --project galapagateway --region us-central1 api-stage
```

Note the container region is `us-central1`. The public endpoint is https://api-stage-592971452831.us-central1.run.app/
