import logging
from flask import Flask

from logging.config import dictConfig



app = Flask(__name__)
wsgi_app = app.wsgi_app
# TODO: Set the app's logger level to "warning"
#   and any other necessary changes
app.logger.setLevel(logging.WARNING)

import FlaskExercise.views