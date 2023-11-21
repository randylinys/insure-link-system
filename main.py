# -*- coding: utf-8 -*-
from app import create_app
from app.route_opt import *
from lib.logger_opt import *

app = create_app()

app.register_blueprint(route_opt)

if __name__ == "__main__":
    logger.info('====The program is starting====')
    app.run(host='0.0.0.0', port=5000)