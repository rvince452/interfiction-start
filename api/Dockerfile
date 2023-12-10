FROM python:3.9-slim-buster

RUN mkdir /app
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt 


COPY . .

EXPOSE 8000


#ENV SET ALLOW_ORIGINS=http://127.0.0.1:80

#CMD ["uvicorn","world.api.main:app", "--host", "0.0.0.0", "--port","8000"]
CMD ["uvicorn","main:app", "--host", "0.0.0.0", "--port","8000"]





