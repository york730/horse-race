import random
import copy


TOTAL_STEP_TO_WIN = 120
TOTAL_ROUND = 10000

racers = {
    "一號":
        [3,4],
    "二號":
        [1,2,6],
    "三號":
        [3,5,6],
    "四號":
        [4,5],
}

effects = {
    "一號": [0,0,0,0,0,0],
    "二號": [0,0,0,0,0,0],
    "三號": [0,0,0,0,0,0],
    "四號": [0,0,0,0,0,0],
}

bids = [4000, 10000, 100000, 20000]

bid_rates = [
    round(sum(bids) / bid, 2) if round(sum(bids) / bid, 2) < 99 else 99 for bid in bids
]
# odds3 = map(lambda x: round(sum(bids)/x, 2) if round(sum(bids)/x, 2) < 99 else 99, bids)
sum_bids = sum(bids) if sum(bids) < 50000 else 50000


def zero_if_negative(a):
    return 0 if a < 0 else a


def break_tie(winners):
    overtime_stepcounter = dict.fromkeys(winners, 0)
    while len(winners) > 1:
        for key in winners:
            overtime_stepcounter[key] += random.choice(racers[key])
        max_value = max(overtime_stepcounter.values())
        winners = [k for k, v in overtime_stepcounter.items() if v == max_value]
    return max(overtime_stepcounter, key=overtime_stepcounter.get)


def race(stepCounter):
    effectsCount = copy.deepcopy(effects)
    while max(stepCounter.values()) < TOTAL_STEP_TO_WIN:
        for key in racers:
            step = random.choice(racers[key])
            extraStep = 0
            if any(v != 0 for v in effectsCount[key]):
                effect = random.choices(
                    population = [i for i, v in enumerate(effectsCount[key]) if v != 0],
                    weights = [v for i, v in enumerate(effectsCount[key]) if v != 0]
                )[0]
                effectsCount[key][effect] -= 1
                if effect == 0:
                    extraStep = random.choice([0, 1, 2])
                elif effect == 1:
                    extraStep = random.choice([2, 3, 4])
                elif effect == 2:
                    extraStep = random.choice(racers[key])
                elif effect == 3:
                    extraStep = random.choice([-2, -1, 0])
                elif effect == 4:
                    extraStep = random.choice([-4, -3, -2])
                elif effect == 5:
                    extraStep = 1
                    step = 0
            stepCounter[key] += zero_if_negative(step + extraStep)

    return list(stepCounter.values())


def repeat_race(results):
    list = []
    for i in range(TOTAL_ROUND):
        step_counter = dict.fromkeys(racers, 0)
        list.append(race(step_counter))
        winner_list = [k for k, v in step_counter.items() if v == max(step_counter.values())]
        winner = max(step_counter, key=step_counter.get) if len(winner_list) == 1 else break_tie(winner_list)
        results[winner] += 1
    print("Average Steps: ", [round(sum(values)/round(TOTAL_ROUND),2) for values in zip(*list)])
    return results


def recommand_bid(results):
    p = [v for v in results.values()]
    print("Bid_Rates: ", bid_rates)
    bids = []
    for i in range(4):
        b_ = bid_rates[i]
        p_ = round(p[i]/TOTAL_ROUND, 4)
        q_ = 1 - p_
        print(
            f"Bid #{i+1}: {int(sum_bids*((p_-q_/b_))):>6} | Bid2 #{i+1}: {int(sum_bids*p_):>6}"
        )
        bids.append(sum_bids*((p_-q_/b_)))
    return bids
