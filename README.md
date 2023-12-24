
# simple-webapp-3 - iteration notes

Previously, both previous branches are Flask (web) and FastAPI (api-backend). They have different requirements and are both docker projects. Following the instructions in notes.txt I can:
1. Run them locally (they must both be running)
1. Deploy both to docker build and run from docker
1. Push to AWS lightsail and redeploy in AWS using the new images.

So now we are just going to update each project to enhance the application.
## Note - I have added a Web/Screenshots folder to show screenshots from the iteration.
This app is more complicated, based on the Flask tutorials. There is a database, authorization and page that lists and lets you add posts. Most of the code is from the tutorial. That all doesn't matter, we are just testing our workflow:

What worked in previous iteration:
### Web
1. Base web with nav menu and user login/logout/register (from Flask tutorial)
1. Worlds list with actions on selected world. Hide edit actions unless user is logged in.
2. Games list with resume/delete action. Hide edit actions unless user is logged in.
3. Bare play menu

### Api
Bare implementation, servers some static JSON to worlds

# Goals for iteration 3
1. Enable real world create, edit and delete functionality.
1. Enable ability to Play a World (create a new game, add it to game list and navigate to play screen). But always creat a new play game.
1. Games list should pull from database.
1. Add base entities/methods to API to support the above


# interfiction-start
This is the start of my ***Interfiction*** project. The general purpose is to implement an interactive fiction website.

## Technologies
Programming language would be Python as I love Python. The website would be as simple as positive and leverage a backend REST API (both in Python)
Planning to host/deploy to AWS, perhaps Lightsail instance.

## Goals
The interactive fiction model should be that of a [Game Book](https://en.wikipedia.org/wiki/Gamebook) - the player should be able to ***easily*** make choices and decisions without tedious typing and searching. That is the player experience. Obviously the experience for writing a new game would be more involed but again simplicity is the goal.

