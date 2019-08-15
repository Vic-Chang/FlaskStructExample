import flask
from flask_restful import Api


app = flask.Flask(__name__)
api = Api(app)
import routes