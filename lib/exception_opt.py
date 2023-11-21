# -*- coding: utf-8 -*-
from lib.logger_opt import *
import sys
import requests

class ExceptionCommon(Exception):
    status_code = 400
    
    def __init__(self, message=None, status_code=None, payload=None):
        Exception.__init__(self)
        self.message = message
        if status_code:
            self.status_code = status_code
        self.payload = payload
        
        ex_type, ex_val, ex_stack = sys.exc_info()
        if ex_type == requests.exceptions.ConnectionError:
            logger.error(f"{message}(ConnectionError)")
        elif ex_type == requests.exceptions.HTTPError:
            logger.error(f"{message}(HTTPError)")
        elif ex_type == requests.exceptions.ConnectTimeout:
            logger.error(f"{message}(ConnectTimeout)")
        elif ex_type == requests.exceptions.ReadTimeout:
            logger.error(f"{message}(ReadTimeout)")
        elif ex_type == requests.exceptions.TooManyRedirects:
            logger.error(f"{message}(TooManyRedirects)")
        else:
            logger.error(self.message, exc_info=True)
            
    def to_dict(self):
        rv = dict(self.payload or ())
        rv['status_code'] = self.status_code
        rv['message'] = self.message
        return rv
        