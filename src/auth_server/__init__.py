import json
import flask
from calendar_client import get_tokens
from flask_restful import Api, Resource
from utils import optional_environ


class CredentialsResource(Resource):
    def get(self):
        return json.loads(get_tokens().to_json())


def serve():
    app = flask.Flask(__name__)
    app.config["DEBUG"] = True
    api = Api(app)
    api.add_resource(CredentialsResource, "/credentials")
    app.run(
        use_reloader=False,
        host="0.0.0.0",
        debug=True,
        threaded=True,
        port=optional_environ('CREDS_PORT', '5000'))
