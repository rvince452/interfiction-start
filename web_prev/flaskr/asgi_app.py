from asgiref.wsgi import WsgiToAsgi
#from . import create_app
from flask import Flask

#flask_app = create_app()
flask_app = Flask(__name__)
asgi_app = WsgiToAsgi(flask_app)