import numpy as np

def average(body):
    mean = np.mean(body[1:-1, 1:-1])
    return mean


def variance(body):
    m, n = body.shape
    mean = average(body)
    var = 1/((m-2)*(n-2)) * np.sum((body[1:-1, 1:-1] - mean)**2)
    return var