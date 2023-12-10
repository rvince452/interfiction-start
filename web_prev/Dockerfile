# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY . .
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt

ENV API_URL="http://api:8000"

# Specify the command to run on container start
# In Docker, it is important to use 0.0.0.0 to listen on all
# CMD [ "flask", "--app", "app", "run","--host=0.0.0.0" ]
# CMD [ "waitress-serve", "--host", "0.0.0.0", "--port", "5000","app:app" ]
# flask --app flaskr run --debug
#CMD ["flask", "--app", "flaskr", "run", "--debug","--host=0.0.0.0"]
CMD [ "waitress-serve", "--host", "0.0.0.0", "--port", "5000","--call","flaskr:create_app" ]