import unittest

from race.predictor import RacePredictor
from race.prediction import racers, repeat_race, recommand_bid

test_data = {
        "一號":
            [[3, 4], [0, 0, 0, 0, 0, 0], 4000],
        "二號":
            [[1, 2, 6], [0, 0, 0, 0, 0, 0], 10000],
        "三號":
            [[3, 5, 6], [0, 0, 0, 0, 0, 0], 100000],
        "四號":
            [[4, 5], [0, 0, 0, 0, 0, 0], 20000],
    }


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
        race_prediction.race()
        # TODO: assert
        # self.assertEqual('foo'.upper(), 'FOO')

    def test_repeat_race(self):
        """

        :return:
            result (dict)
        """
        race_prediction = RacePredictor(test_data)
        race_prediction.repeat_race()
        # TODO: assert
        # self.assertEqual('foo'.upper(), 'FOO')

    def test_recommend_bid(self):
        """

        :return:
            bids (list)
        """
        race_prediction = RacePredictor(test_data)
        race_prediction.recommend_bid()
        # TODO: assert
        # self.assertEqual('foo'.upper(), 'FOO')

    def test_predict(self):
        """

        :return:
            [results, bid] (list)
        """
        race_prediction = RacePredictor(test_data)
        race_prediction.predict()
        # TODO: assert
        # self.assertEqual('foo'.upper(), 'FOO')


if __name__ == '__main__':
    unittest.main()
