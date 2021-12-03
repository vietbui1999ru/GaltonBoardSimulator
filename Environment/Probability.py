import math

import matplotlib.pyplot as plt
import numpy as np
import random
from scipy.stats import norm

# looks pretty with the following values
TOTAL_BALLS = 50000
TOTAL_LINES = 16


# def plot_galton(dist, lines):
#     plt.bar([str(i) for i in range(0, lines + 1)], dist[0:lines + 1])
#     plt.xticks([])

def pdf(x):
    mean = np.mean(x)
    std = np.std(x)
    y_out = 1 / (std * np.sqrt(2 * np.pi)) * np.exp(- (x - mean) ** 2 / (2 * std ** 2))
    return y_out


def galton(balls, lines) -> list:
    dist = [0] * ((lines * 2) + 1)

    for ball in range(0, balls):
        total = 0

        for line in range(1, lines + 1):
            outcome = random.uniform(0, 1)
            if outcome >= 0.5:
                total += 1
            else:
                total -= 1
        dist[total + lines] += 1

    for i in range(0, lines + 1):
        dist[i] = dist[i * 2]

    return dist[0:lines + 1]


class Prob:
    def __init__(self, num_balls=TOTAL_BALLS, num_lines=TOTAL_LINES):
        self.num_balls = num_balls
        self.num_lines = num_lines

    def start_p(self):
        dist = galton(self.num_balls, self.num_lines)
        # plot_galton(dist, self.num_lines)
        return dist

    def get_lines(self):
        return self.num_lines

    def bell_curve(self):

        # A custom function to calculate
        # probability distribution function

        # To generate an array of x-values
        x = np.arange(1, self.get_lines(), 0.001)

        # To generate an array of
        # y-values using corresponding x-values
        print(np.median(self.start_p()))
        y = norm.pdf(x, np.median(self.start_p()), 1)

        # Plotting the bell-shaped curve
        # plt.style.use('seaborn')
        # plt.figure(figsize=(6, 6))
        # plt.plot(x, y, color='black',
        #          linestyle='dashed')
        #
        # plt.scatter(x, y, marker='o', s=25, color='red')
        print(y)
        return x, y


if __name__ == "__main__":

    a = (galton(TOTAL_BALLS, TOTAL_LINES))
    print(Prob().start_p())
    print(a)

    print(Prob().get_lines())
    Prob().bell_curve()