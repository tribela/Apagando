import os

import flask
import flask_sse

app = flask.Flask(__name__)
app.config['REDIS_URL'] = os.getenv('REDIS_URL')
app.register_blueprint(flask_sse.sse, url_prefix='/stream')


@app.route('/')
def index():
    return flask.render_template('index.html')


@app.route('/send')
def send_msg():
    flask_sse.sse.publish({
        'message': 'Hello, World!',
    }, type='greeting')
    return 'Sent message'
