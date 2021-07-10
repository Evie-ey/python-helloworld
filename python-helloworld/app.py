import logging
from flask import Flask, jsonify, make_response, json
app = Flask(__name__)


@app.route("/")
def hello():
    return "Hello World!"


# @app.route("/status")
# def healthCheck():
#     data = {'user': 'Evie', 'result': 'Ok-healthy'}
#     return make_response(jsonify(data), 200)


# @app.route("/metrics")
# def getMetrics():
#     data = {'user': 'Evie', 'data': {'UserCount': 140, 'userCountActive': 23}}
#     return make_response(jsonify(data), 200)

@app.route('/status')
def status():
    response = app.response_class(
        response=json.dumps({"result": "OK - healthy"}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Status request successful')
    return response


@app.route('/metrics')
def metrics():
    response = app.response_class(
        response=json.dumps({"status": "success", "code": 0, "data": {
                            "UserCount": 140, "UserCountActive": 23}}),
        status=200,
        mimetype='application/json'
    )

    app.logger.info('Metrics request successful')

    return response


if __name__ == "__main__":
    logging.basicConfig(filename='app.log', level=logging.DEBUG)
    app.run(host='0.0.0.0')
