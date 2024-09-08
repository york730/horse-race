import unittest
import asyncio

from race.predictor import RacePredictor
from race.prediction import racers, repeat_race, recommand_bid

from test import test_data


class TestPrediction(unittest.TestCase):
    """Functional code

    """

    def test_integration_prediction(self):
        """

        :return:
            [results, bid] (list)
        """
        results = dict.fromkeys(racers, 0)
        repeat_race(results)
        print(results)
        bid = recommand_bid(results)
        # TODO: [results, bid]
        # TODO: assert
        # self.assertEqual('foo'.upper(), 'FOO')


class TestPredictor(unittest.TestCase):

    def test_race(self):
        """

        :return:
            list
        """
        race_prediction = RacePredictor(test_data)
        step_counter = dict.fromkeys(test_data, 0)
        result = race_prediction.race(step_counter)
        self.assertTrue(75 < result[0] <= 100)
        self.assertTrue(50 < result[1] <= 100)
        self.assertTrue(115 < result[2] <= 130)
        self.assertTrue(99 < result[3] <= 130)

    def test_repeat_race(self):
        """

        :return:
            result (dict)
        """
        race_prediction = RacePredictor(test_data)
        result = asyncio.run(race_prediction.repeat_race())
        # result = race_prediction.repeat_race()
        self.assertTrue(result.get("一號") < 5)
        self.assertTrue(result.get("二號") < 10)
        self.assertTrue(7000 < result.get("三號") < 8000)
        self.assertTrue(2000 < result.get("四號") < 3000)

    def test_recommend_bid(self):
        """

        :return:
            bids (list)
        """
        race_prediction = RacePredictor(test_data)
        bids = race_prediction.recommend_bid()
        self.assertTrue(-1550 < bids[0] < -1400)
        self.assertTrue(-4000 < bids[1] < -3500)
        self.assertTrue(-40000 < bids[2] < -35000)
        self.assertTrue(-8000 < bids[3] < -7000)

    def test_predict(self):
        """

        :return:
            [results, bid] (list)
        """
        race_prediction = RacePredictor(test_data)
        race_prediction.predict()
        result = race_prediction.results
        self.assertTrue(result.get('一號') < 100)
        self.assertTrue(result.get('二號') < 100)
        self.assertTrue(5000 < result.get('三號') < 10000)
        self.assertTrue(2000 < result.get('四號')< 5000)


if __name__ == '__main__':
    unittest.main()
