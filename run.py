import flask
from flask_restful import Api
from flask_bootstrap import Bootstrap

app = flask.Flask(__name__)
api = Api(app)
Bootstrap(app)
import routes