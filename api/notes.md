# APP = REST API 

We will use FastApi to construct our rest api
[Fast API](https://fastapi.tiangolo.com)


pip install fastapi

The tutorial uses uvicorn but uvicorn does not run on windows so I can't test it, so I prefer to use waitress

To run on Waitress:
waitress-serve main.app
http://http://127.0.0.1:8080/

waitress-serve --call flaskr:create_app 
waitress-serve --host 127.0.0.1 --call flaskr:create_app
waitress-serve --host 0.0.0.0 --call flaskr:create_app 
waitress-serve --host 0.0.0.0 --port 5000 --call flaskr:create_app

BUT it doesn't work. Waitress supports only WSGI while FASTAPI wants ASGI. From google, it seems ASGI might be the better way, so trying to find a server that:
1) Is ASGI
2) Will work with Flask
3) Is available for both Windows and Linux

I WAS NOT ABLE TO DO THIS. SO I WILL USE UVICORN with API and WAITRESS WITH WEB

Flask can run ASGI with a converter:
https://flask.palletsprojects.com/en/2.2.x/deploying/asgi/

Try UVICORN
To install with standard extras:
pipen install Uvicorn[standard]
On windows local - do not specify host/port, just do default

uvicorn main:app
uvicorn main:app --reload
http://127.00.0.1:8000
http://127.00.0.1:8000/docs
http://127.0.0.1:8000/redoc

