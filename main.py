from flask      import Flask
from flask      import request
from jwtoken    import Jwtoken
import logging
import json

import ssl

try:
    _create_unverified_https_context = ssl._create_unverified_context
except AttributeError:
    pass
else:
    ssl._create_default_https_context = _create_unverified_https_context

logging.basicConfig(level=logging.DEBUG)
app             = Flask(__name__)

default_error   = json.dumps({"errorCode": 500, "errorMessage": "System failure", "displayMessage": "Oops something went wrong !"})
logging.info("python code started")


@app.route("/v1")
def working():
    return {"response":"authorization service running"}


# otp create related actions
@app.route("/v1/getJWT", methods=["GET"])
def getjwt():
    try:
        if request.method == "GET":
            number      = request.args["number"]
            logging.debug("incoming request: number = " + str(number))
            response    = json.dumps(Jwtoken.make_token(number))
            return response
    except RuntimeError as e:
        logging.critical("failure in v1/getJWT with error: " + str(e))
        return default_error


if __name__ == '__main__':
    app.run(host='0.0.0.0', debug=True, port=8080, ssl_context='adhoc')
