from flask import Flask

from race.prediction import *
from race.predictor import *

from test import test_data

# Give up Sanic temporarily...
app = Flask(__name__)


@app.route('/')
def home():
    return 'Hello, World!'


@app.route('/api/prediction/')
def prediction():
    # TODO: haven't process return data
    results = dict.fromkeys(racers, 0)
    repeat_race(results)
    print(results)
    bid = recommand_bid(results)
    return 'About'


@app.route('/api/predictor/')
def predictor():
    # TODO: request: params should pass from Front-end
    race_prediction = RacePredictor(test_data)
    response = race_prediction.predict()
    response = "\n".join(response)
    return response
