import json
from bottle import *
import bottle
from file_server import *


# Returns static file. Used for getting JavaScript files from /scripts folder
@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='../scripts/')


# Returns worker page
@bottle.get('/')
def index():
    return static_file('index.html', root='../HTML/')


# Read
@bottle.get('/read')
def bottle_read():
    return json.dumps(read())
    # return read()
    # return str(read())


run(host='127.0.0.1', port=8080, debug=True)