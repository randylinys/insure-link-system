# -*- coding: utf-8 -*-
from flask import Blueprint, request, jsonify
from flask_cors import cross_origin
from lib.exception_opt import ExceptionCommon
from lib.logger_opt import *
import lib.opt as opt

route_opt = Blueprint('route_opt', __name__)

### 保戶查詢
@route_opt.route('/api/policyholders', methods=['GET'])
@cross_origin()
def policyholders():
    code = request.args.get('code')
    response = opt.policyholders(code)
    return jsonify(response), 200
    
### 保戶上層查詢
@route_opt.route('/api/policyholders/<code>/top', methods=['GET'])
@cross_origin()
def policyholders_top(code):
    response = opt.policyholders_top(code)
    return jsonify(response), 200
    