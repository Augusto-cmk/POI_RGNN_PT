import statistics as st
import math
import numpy as np

from .t_distribution import T_Distribution
import scipy.stats as stt

def t_distribution_test(x, confidence=0.95):
    n = len(x)
    decimals = 1
    mean = round(st.mean(x), decimals)
    liberty_graus = n
    s = st.stdev(x)
    alfa = 1 - confidence
    column = 1 - alfa / 2
    t_value = T_Distribution().find_t_distribution(column, liberty_graus)
    average_variation = round((t_value * (s / math.pow(n, 1 / 2))), decimals)
    average_variation = str(average_variation)
    while len(average_variation) < decimals + 3:
        average_variation = "0" + average_variation

    mean = str(mean)
    while len(mean) < decimals + 3:
        mean = "0" + mean

    ic = stt.t.interval(alpha=0.95, df=len(x) - 1, loc=np.mean(x), scale=stt.sem(x))
    l = round(ic[0], decimals)
    r = round(ic[1], decimals)

    return str(mean) + u"\u00B1" + average_variation