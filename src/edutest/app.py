import sys
import logging

import json_logging
from flask import Flask

from .constants import SUCCESSFUL_INCREASE_MSG

app = Flask(__name__)

json_logging.init_flask(enable_json=True)
json_logging.init_request_instrument(app)

logger = logging.getLogger('json-logger')
logger.setLevel(logging.DEBUG)
logger.addHandler(logging.StreamHandler(sys.stdout))

counter = 0 # not a constant ; pylint: disable=invalid-name

@app.route('/')
def index():
    return 'ok'

@app.route('/inc', methods=['POST'])
def increase():
    global counter
    current_counter = counter
    counter += 1
    return {
        'msg': SUCCESSFUL_INCREASE_MSG,
        'prev': current_counter,
        'new': counter
    }, 201

@app.route('/info')
def info():
    return {'counter': counter}
