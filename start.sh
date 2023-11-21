#!/bin/bash
cd sample
gunicorn --workers=4 --threads=4 --bind=0.0.0.0:5000 --log-level debug --capture-output --enable-stdio-inheritance wsgi:app