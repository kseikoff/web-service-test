from flask import Flask, request, abort

from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

from flask_talisman import Talisman

import yaml


app = Flask(__name__)
talisman = Talisman(app)
limiter = Limiter(
    get_remote_address,
    app=app,
    default_limits=["200 per day", "50 per hour"],
    storage_uri="redis://localhost:6379",
    storage_options={"socket_connect_timeout": 30},
    strategy="moving-window",
)

DEFAULT_NAME = "You"
DEFAULT_MESSAGE = "Have a nice day"

with open('config.yaml', 'r') as file:
    data = yaml.safe_load(file)

# API_KEY = data['some_test']['some_syms']
# LINK = "http://localhost:5000/"
# EXTERNAL_LINK = "web-service-test.online"
go_debug = bool(int(data['some_test']['dbg']))


# @app.before_request
# def check_api_key():
#     key = request.headers.get("X-API-Key")
#     if key != API_KEY:
#         abort(403)


@app.route("/")
@limiter.limit("1/second", override_defaults=False)
def test_get():
    name = request.args.get("name")
    message = request.args.get("message")

    if not name:
        name = DEFAULT_NAME
    if not message:
        message = DEFAULT_MESSAGE

    return f"Hello {name}! {message}!", 200


if __name__ == "__main__":
    app.run(host="127.0.0.1", port=5000, debug=go_debug)
