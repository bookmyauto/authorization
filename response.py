import logging
import json


class Response:

    default_error = json.dumps({"errorCode": 500, "errorMessage": "System failure", "displayMessage": "Oops something went wrong !"})

    # Makes response
    @staticmethod
    def make_response(http_code, message, display_message, **kwargs):
        result              = {"httpCode": str(http_code), "message": str(message),
                               "displayMessage": str(display_message), "data": {}}
        logging.info("  Result maker has received")
        for key, value in kwargs.items():
            result["data"][key]     = value
        return result
