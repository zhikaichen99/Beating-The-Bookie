import pandas
import numpy as np
from scipy.stats import norm

def player_over_probability(stat, threshold, df):
    stat_list = df[stat].values.tolist()
    stat_list = [int(x) for x in stat_list]
    # calculate the mean and the standard deviation
    mean = np.mean(stat_list)
    stddev = np.std(stat_list)

    # estimate the probability of exceeding the threshold
    probability = 1 - norm.cdf(threshold, loc = mean, scale= stddev)
    return probability 