from bottle import *
import bottle


# Returns static file. Used for getting JavaScript files from /scripts folder
@bottle.get('/scripts/:filename#.*#')
def send_static(filename):
    return static_file(filename, root='./scripts/')


# Returns worker page
@bottle.get('/')
def index():
    return static_file('index.html', root='./HTML/')


# Read
@bottle.get('/read')
def read():
    # return '2'
    # return {'name': 'Lab1', 'state': 'Completed'}
    return '[{"name": "Lab1", "state": "Completed"}, {"name": "Lab2", "state": "Completed"}]'


run(host='127.0.0.1', port=8080, debug=True)