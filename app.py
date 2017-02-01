import time

import flask

import lights

app = flask.Flask(__name__)

controller = lights.Lights()

# Blink once to notify boot
for i in range(len(controller)):
    try:
        controller[i] = 1
        time.sleep(1)
        controller[i] = 0
    except:
        pass


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/status')
def status():
    return flask.jsonify([
        controller[i]
        for i in range(len(controller))
    ])


@app.route('/switch/<int:number>', methods=['GET'])
def get_switch_status(number):
    return flask.jsonify(controller[number])


@app.route('/switch/<int:number>', methods=['PUT', 'DELETE', 'POST'])
def set_switch_status(number):
    mapping = {
        'PUT': 1,
        'DELETE': 0,
    }

    if flask.request.method in mapping:
        switch = mapping[flask.request.method]
    elif flask.request.method == 'POST':
        data = flask.request.json or flask.request.form
        switch = int(data.get('switch'))

    controller[number] = switch
    return 'OK'
