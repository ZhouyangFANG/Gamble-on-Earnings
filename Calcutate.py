import random
import math
import matplotlib.pyplot as plt
import numpy as np

NUMBER_OF_EARNING_REPORTS = 100
PROBABILITY_OF_WIN = 0.7
WINNING_PROFIT = 0.05
FAILURE_LOSS = 0.05
MAX_DIVISION = 5
NUMBER_OF_SAMPLES = 100

def main():
    number_of_division = np.arange(1, MAX_DIVISION + 1)

    final_cash = np.zeros(MAX_DIVISION)

    random.seed(1)
    for division_minus_one in range(0, MAX_DIVISION):
        rounds = math.ceil(NUMBER_OF_EARNING_REPORTS/(division_minus_one + 1))


        # for given division, stores the final value of each sample.
        sample_list = np.zeros(NUMBER_OF_SAMPLES)

        for sample in range(NUMBER_OF_SAMPLES):

            # evenly divide the current cash, eg. [5.6, 5.6, 5.6]
            cash_division = np.ones(division_minus_one + 1) \
                / (division_minus_one + 1)

            for report in range(rounds):
                for cash_number in range(division_minus_one + 1):
                    cash_division[cash_number] = cash_division[cash_number] \
                        * after_report()
            cash_division.fill(np.mean(cash_division))

            sample_list[sample] = np.sum(cash_division)
    
        final_cash[division_minus_one] = np.mean(sample_list)
        return_rate_for_every_report = np.float_power(final_cash, \
            1 / NUMBER_OF_EARNING_REPORTS) - 1
   
    plot(number_of_division, return_rate_for_every_report)

def plot(data1, data2):
    fig, ax = plt.subplots()
    ax.plot(data1, data2)
    plt.show()
    return None

def after_report():
    rand = random.random()
    return (1 + WINNING_PROFIT) if rand < PROBABILITY_OF_WIN \
        else (1 - FAILURE_LOSS)


if __name__ == '__main__':
    main()

