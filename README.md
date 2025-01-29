# explorer-core
Docker compose of collections explorer core (Django API container, mySQL container, nginx container)
Nginx depends on Django web, Django web relies on mySQL

Docker Compose version v2.26.1-desktop.1
Docker Engine - Community version 27.2.0


>Things to modify before build:

>_`.env` (Request from [@zhucchininoodles](https://github.com/zhucchininoodles))_
>- add .env file to root of Django project folder: _explorer-core/.env_
>
>`_collections_app_api/static/_`
>- create a _static_ folder in _collections_app_api_ folder; add your static files/scans (example file _casxlogo.png_ included)

---
# Local Deployment
There is a shell script _dc_start.sh_ to make building and starting more convenient:
```bash
./dc_start.sh up
``` 
This will build the project with project label _galapagateway_api_

The same shell script can be used to stop and remove the Docker containers, volumes, builder cache:
```bash
./dc_start.sh down
```

...And to occassionally, fully prune Docker resources and builder cache/layers tied to this project:
```bash
./dc_start.sh prune
```
* _Should_ only prune resources related to this project only. ***DO*** double-check before cleaning.....
* Still tweaking "cleanup" part of dc_start.sh

* API runs on _0.0.0.0_ after successful deployment.

Visit _0.0.0.0/api/docs_ to view API document (_/collections_app_api/collections_schema.yaml_).

Static files served through nginx on _0.0.0.0/static/_

---

# GCP Deployment *(WIP)*
 
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

----

# Django Admin Panel / Occurrences Data Modification
Pre-existing _Occurrences_ records of _collectionsdb_ can be changed/modified, or new occurrences can be created and added *(WIP)*, through the Django admin panel, `0.0.0.0/admin`. 

Contact [@zhucchininoodles](https://github.com/zhucchininoodles) for API admin login credentials.