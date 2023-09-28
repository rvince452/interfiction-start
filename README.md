# status: IN PROGRESS
# simple-webapp-2
This app is more complicated, based on the Flask tutorials. There is a database, authorization and page that lists and lets you add posts. Most of the code is from the tutorial. That all doesn't matter, we are just testing our workflow:

First iteration - use flask tutorial code
1. Delete all the pipenv files as we are starting over. pipenv will create a new environment when we use it.
1. With pipenv install Flask and the other suggested packages. Install waitress. Now we have new pipenv files.
1. Test locally. This works.
1. Create a new Requirements.txt from pipenv - we need this for docker.
1. Deploy to docker. Works.
1. Deploy to AWS works.

Next iteration - same as above but add
1. Style css static file and bootstrap js/css - Works
1. Need to add my own pages next



# interfiction-start
This is the start of my ***Interfiction*** project. The general purpose is to implement an interactive fiction website.

## Technologies
Programming language would be Python as I love Python. The website would be as simple as positive and leverage a backend REST API (both in Python)
Planning to host/deploy to AWS, perhaps Lightsail instance.

## Goals
The interactive fiction model should be that of a [Game Book](https://en.wikipedia.org/wiki/Gamebook) - the player should be able to ***easily*** make choices and decisions without tedious typing and searching. That is the player experience. Obviously the experience for writing a new game would be more involed but again simplicity is the goal.

