# -*- coding: utf-8 -*-
from flask import Flask, jsonify
from lib.exception_opt import ExceptionCommon

def create_app():
    app = Flask(__name__)
    app.config['JSON_AS_ASCII'] = False
    
    @app.errorhandler(ExceptionCommon)
    def handle_invalid_usage(error):
        response = jsonify(error.to_dict())
        response.status_code = error.status_code
        return response
        
    @app.errorhandler(404)
    def page_not_found(error):
        response = dict(status_code=404, message='404 Not Found')
        return jsonify(response), 404
        
    @app.errorhandler(500)
    def handle_500(error):
        response = dict(status_code=500, message='500 Error')
        return jsonify(response), 500
        
    return app
    