import random
import copy

TOTAL_STEP_TO_WIN = 120
TOTAL_ROUND = 10000


class RacePredictor(object):

    def __init__(self, data):
        self.data = data
        self.results = dict.fromkeys(data, 0)
        self.step_counter = dict.fromkeys(data, 0)
        self.effects_count = copy.deepcopy({k: v[1] for k, v in data.items()})
        self.effect_choices = {
                0: [0, 1, 2],
                1: [2, 3, 4],
                2: lambda v: random.choice(v[0]),
                3: [-2, -1, 0],
                4: [-4, -3, -2],
                5: (lambda: (1, 0))
            }
        self.bids = list(map(lambda x: x[2], data.values()))
        self.bid_rates = [
                round(sum(self.bids) / bid, 2) if round(sum(self.bids) / bid, 2) < 99 else 99 for bid in self.bids
        ]
        self.sum_bids = sum(self.bids) if sum(self.bids) < 50000 else 50000

    @staticmethod
    def zero_if_negative(a):
        return 0 if a < 0 else a

    def break_tie(self, winners):
        overtime_stepcounter = dict.fromkeys(winners, 0)
        while len(winners) > 1:
            for key in winners:
                overtime_stepcounter[key] += random.choice(self.data[key][0])
            max_value = max(overtime_stepcounter.values())
            winners = [k for k, v in overtime_stepcounter.items() if v == max_value]
        return max(overtime_stepcounter, key=overtime_stepcounter.get)

    def race(self):
        # TODO: effectsCount need to initialize the value each for loop
        # TODO: step_counter need to initialize the value each for loop
        # effectsCount = copy.deepcopy(effects)
        while max(self.step_counter.values()) < TOTAL_STEP_TO_WIN:
            for key, value in self.data.items():
                step = random.choice(value[0])
                extra_step = 0
                if any(v != 0 for v in self.effects_count[key]):
                    effect = random.choices(
                        population=[i for i, v in enumerate(self.effects_count[key]) if v != 0],
                        weights=[v for i, v in enumerate(self.effects_count[key]) if v != 0]
                    )[0]
                    self.effects_count[key][effect] -= 1
                    if effect in self.effect_choices:
                        if effect == 5:
                            extra_step, step = self.effect_choices[5]()
                        else:
                            extra_step = self.effect_choices[effect] if isinstance(self.effect_choices[effect], list) else \
                            self.effect_choices[effect](value)
                self.step_counter[key] += self.zero_if_negative(step + extra_step)
        return list(self.step_counter.values())

    def repeat_race(self):
        list = []
        for i in range(TOTAL_ROUND):
            list.append(self.race())
            winner_list = [k for k, v in self.step_counter.items() if v == max(self.step_counter.values())]
            # TODO: debugging 永遠跳不進 self.break_tie
            winner = max(self.step_counter, key=self.step_counter.get) if len(winner_list) == 1 else self.break_tie(winner_list)
            self.results[winner] += 1
        print("Average Steps: ", [round(sum(values) / round(TOTAL_ROUND), 2) for values in zip(*list)])
        return self.results

    def recommend_bid(self):
        p = [v for v in self.results.values()]
        print("Bid_Rates: ", self.bid_rates)
        bids = []
        for i in range(4):
            b_ = self.bid_rates[i]
            p_ = round(p[i] / TOTAL_ROUND, 4)
            q_ = 1 - p_
            print(
                f"Bid #{i + 1}: {int(self.sum_bids * ((p_ - q_ / b_))):>6} | Bid2 #{i + 1}: {int(self.sum_bids * p_):>6}"
            )
            bids.append(self.sum_bids * ((p_ - q_ / b_)))
        return bids

    def predict(self):
        """API @route: /api/
        - process request body
        - prediction logics
        - response
        """
        self.repeat_race()
        print(self.results)
        bid = self.recommend_bid()
        return [self.results, bid]
