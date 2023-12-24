CD API 
docker build --tag web-fastapi-2 .

CD ..
CD WEB
docker build --tag web-flask-2 .


CD ..
docker-compose build 
docker-compose up --build