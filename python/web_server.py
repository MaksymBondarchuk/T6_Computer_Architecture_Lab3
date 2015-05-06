import json
from bottle import *
import bottle
from file_server import *

result = ''

# Returns static file. Used for getting JavaScript files from /scripts folder
@bottle.get('/scripts/:filename#.*#')
def send_static_javascript(filename):
    return static_file(filename, root='../scripts/')


# Returns static file. Used for getting CSS files from /styles folder
@bottle.get('/styles/:filename#.*#')
def send_static_css(filename):
    return static_file(filename, root='../styles/')


# Returns worker page
@bottle.get('/')
def index():
    return static_file('index.html', root='../HTML/')


# READ
@get('/read')
def bottle_read():
    return json.dumps(read())


# DELETE
@post('/delete')
def bottle_delete():
    global result
    result = delete(request.body.read())
    if result == result_OK:
        result = 'Deleted successfully'


# CREATE
@post('/add')
def bottle_add():
    name = request.forms.get('name')
    about = request.forms.get('about')
    state = request.forms.get('state')
    global result
    result = add(name, about, state)
    if result == result_OK:
        result = 'Added successfully'


# UPDATE
@post('/update')
def bottle_update():
    name = request.forms.get('name')
    field = request.forms.get('field')
    value = request.forms.get('value')
    global result
    result = update(name, field, value)
    if result == result_OK:
        result = 'Changed successfully'


# Returns result of the last operation
@get('/result')
def bottle_read():
    # print(result)
    if result == error_file_exists:
        return json.dumps({'color': 'red', 'result': result})
    return json.dumps({'color': 'green', 'result': result})


run(host='127.0.0.1', port=8080, debug=True)