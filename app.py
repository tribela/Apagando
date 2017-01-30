import os

import flask
import flask_sse

import lights

app = flask.Flask(__name__)
app.config['REDIS_URL'] = os.getenv('REDIS_URL')
app.register_blueprint(flask_sse.sse, url_prefix='/stream')

controller = lights.Lights()


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


@app.route('/switch/<int:number>', methods=['PUT', 'DELETE'])
def set_switch_status(number):
    mapping = {
        'PUT': 1,
        'DELETE': 0,
    }

    if flask.request.method in mapping:
        controller[number] = mapping[flask.request.method]
        return 'OK'


@app.route('/send')
def send_msg():
    flask_sse.sse.publish({
        'message': 'Hello, World!',
    }, type='greeting')
    return 'Sent message'
