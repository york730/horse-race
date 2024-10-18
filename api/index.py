from flask import Flask
from flask import request
from flask import jsonify
from flask_cors import CORS
from flask_cors import cross_origin

from race.prediction import *
from race.predictor import *

from test import test_data

# Give up Sanic temporarily...
app = Flask(__name__)
CORS(app)
CORS(app, resources={r"/api/*": {"origins": "http://localhost:3000"}})
# TODO: add github page url for CORS.


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/test/predictor/')
def test_predictor():
    race_prediction = RacePredictor(test_data)
    response = race_prediction.predict()
    response = "\n".join(response)
    return response


@app.route('/api/prediction/')
def prediction():
    # TODO: haven't process return data
    results = dict.fromkeys(racers, 0)
    repeat_race(results)
    print(results)
    bid = recommand_bid(results)
    return "Haven't finish the development!"


@app.route('/api/predictor/', methods=['POST'])
@cross_origin()
def predictor():
    data = request.json
    data = data.get("data")
    race_prediction = RacePredictor(data)
    response = race_prediction.predict()
    return jsonify({
        'data': response
    })


# Debugging Mode
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
