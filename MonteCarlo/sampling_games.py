"""This module contains examples of Monte Carlo direct sampling techniques."""
import numpy as np

def direct_pi(num_trials):
    '''
    This Function uses Monte Carlo direct sampling to approximate the value of
    pi.

    INPUTS:
        num_trials: The number of positions to be sampled

    OUTPUTS: The approximation of Pi
    '''
    num_hits = 0
    for i in xrange(num_trials):
        x = np.random.uniform(0, 1)
        y = np.random.uniform(0, 1)

        if x**2 + y**2 <= 1:
            num_hits += 1

    return float(num_hits) / num_trials * 4


def markov_pi(num_trials, delta):
    """
    This Function uses Monte Carlo markov sampling to approximate the value of
    pi.

    INPUTS:
        num_trials: The number of positions to be sampled
        delta: The range of step size

    OUTPUTS: The approximation of Pi
    """
    num_hits = 0
    x = 1
    y = 1
    for i in xrange(num_trials):
        del_x = np.random.uniform(-delta, delta)
        del_y = np.random.uniform(-delta, delta)

        if np.absolute(x + del_x) < 1 and np.absolute(y + del_y) < 1:
            x += del_x
            y += del_y

        if x**2 + y**2 < 1:
            num_hits += 1

    return float(num_hits) / num_trials * 4


def direct_buffon_needle(n_trials, a, b):
    """
    This Function uses Monte Carlo direct sampling and buffon's needle problem
    to apprixmate the value of Pi.

    INPUTS:
        num_trials: The number of positions to be sampled
        a: lengh of the needle
        b: width of the floorboards

    OUTPUTS: The approximation of Pi
    """
    n_hits = 0
    for i in xrange(n_trials):
        n_hits += buffon_needle_patch(a, b)

    mean = float(n_hits)/n_trials
    return (a/b)*(2/mean)



def buffon_needle_patch(a, b):
    """
    Helper function that determines a single hit of buffon's needle.

    INPUTS:
        a: lengh of the needle
        b: width of the floorboards

    OUTPUTS: If there was a hit
    """
    x_center = np.random.uniform(0, b/2)
    upsilon = 10.0
    while upsilon > 1.0:
        del_x = np.random.uniform(0, 1)
        del_y = np.random.uniform(0, 1)
        upsilon = np.sqrt(del_x**2 + del_y**2)

    x_tip = x_center - (a/2) * del_x/upsilon
    if x_tip < 0:
        hit = 1
    else:
        hit = 0

    return hit
