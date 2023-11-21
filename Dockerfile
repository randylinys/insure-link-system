FROM python:3.7.11
MAINTAINER randylinys

WORKDIR /

RUN pip3 install \
    flask==2.0.2 \
    flask_cors==3.0.10 \
    gunicorn==21.2.0 \
    requests==2.24.0
    
ADD . /sample

CMD ["/bin/bash", "/sample/start.sh"]
