# General
This project has the following subprojects:
1. api - restapi - python
1. web - user interface - python
The web app will look for the api using the following environmental variable: API_URL
SET API_URL=http://127.0.0.1:8000

Each project can be built into a Docker image and run/tested under Docker

The Docker containers can then be sent to an Amazon Lightsail Container Service (each as its own container)

# Building and running in Docker
Choose a 'tag name' for each project and then run the following commands

From web folder:
docker build --tag web-flask-3 .

From api folder:
docker build --tag web-fastapi-3 .

Now the docker images are built. You can tie them together and run the docker application:

From parent folder:
docker-compose build 
docker-compose up --build

OR 
RUN BUILD_RUN_DOCKER.BAT from parent folder 

# Test in Docker
With Docker, you can test both web and api. However, note that the web refers to the api in a different way. See the web docketfile:
    ENV API_URL="http://api:8000"

WEB: 
DO NOT USE http://0.0.0:5000 - it does not work
INSTEAD USE:
http://localhost:5000
To test it can talk to API:
http://localhost:5000/world/

API:
http://localhost:8000
http://localhost:8000/items 

# To copy images to Lightsail

Run this command to get the image ids of the two new images. Make sure you find the recent ones and not old ones
docker images



