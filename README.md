# django-docker-gunicorn-nginx

This repository is a simple production ready Django boilerplate webapp based on **Docker-Postgresql-Gunicorn-Nginx**

It contains a very very simple django app.


# Prerequisites ?

 - Python
 - Docker and Docker-Compose

# How to Use ?

 1. Clone the repo
 2. Make sure you are on the project root directory (where the ***docker-compose.yaml*** file is located)
 3. Build & run the app by typing the following command
	 

	    sudo docker-compose up -d  --build

## NB:

	+- Before running the app, make sure you update:

		+- The `.env` file environment variables values.

		+- The `docker-compose.yaml` file with your own environement variables values.
