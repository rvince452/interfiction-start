# Set base image (host OS)
FROM python:3.8-alpine

# By default, listen on port 5000
EXPOSE 5000

# Set the working directory in the container
WORKDIR /app

# Copy the dependencies file to the working directory
COPY web .
COPY requirements.txt .

# Install any dependencies
RUN pip install -r requirements.txt


# Specify the command to run on container start
# CMD [ "python", "./app.py" ]
# flask --app flaskr run --debug
CMD ["flask", "--app", "flaskr", "run", "--debug"]