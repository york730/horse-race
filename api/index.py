from flask import Flask
from flask import request

from race.prediction import *
from race.predictor import *

from test import test_data

# Give up Sanic temporarily...
app = Flask(__name__)


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
def predictor():
    data = request.json
    data = data.get("data")
    race_prediction = RacePredictor(data)
    response = race_prediction.predict()
    response = "\n".join(response)
    return response


# Debugging Mode
if __name__ == '__main__':
    app.run(host="127.0.0.1", port=8000)
