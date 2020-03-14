"""
                Description : This code handles operationd relted to JWT
                Author      : Rahul Tudu
"""
import  jwt
import  logging
import  json
from    datetime import datetime
from    response import Response


class Jwtoken:

    # ----------------------------------------------------------------------------------------------------------------------------------------------------- #
    #                                                           MAKE JWT TOKEN
    # ----------------------------------------------------------------------------------------------------------------------------------------------------- #
    @staticmethod
    def make_token(number):
        try:
            timestamp   = datetime.timestamp(datetime.now())
            payload     = {'number': str(number), 'iat': timestamp, 'exp': timestamp + (3 * 24 * 60 * 60)}
            token       = jwt.encode(payload, 'mandolin', algorithm='HS256')
            token       = token.decode("utf-8")
            print(token)
            response    = Response.make_response(200, "", "", token = token)
            print(response)
            return response
        except Exception as e:
            logging.error("Error in making token: " + str(e))
            return Response.default_error
