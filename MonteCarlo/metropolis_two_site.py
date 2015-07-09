""" This Module implements the metropoplis two site problem"""
import numpy as np

def markov_next_site(current_site, propability_of_site):
    if current_site == 0:
        next_site = 1
    else:
        next_site = 0

    upsilon = propability_of_site(next_site) / propability_of_site(current_site)

    if np.random.uniform(low=0.0, high=1.0, size=1) < upsilon:
        current_site = next_site

    return current_site


def play_metropolis_two_site(starting_pos, prob_0, prob_1, num_iterations):
    determine_probabilities = lambda site: prob_0 if site == 0 else prob_1
    c_site = starting_pos
    time_spent = {0: 0, 1:0}
    for i in xrange(num_iterations):
        c_site = markov_next_site(c_site, determine_probabilities)
        time_spent[c_site] += 1

    return time_spent

if __name__ == '__main__':
    print play_metropolis_two_site(0, 0.2, 0.8, 10000)
