import numpy as np

def reject_sampling_finite(probabilites):
    upsilon = 999
    k = 0
    while upsilon > probabilites[k]:
        prob_max = np.amax(probabilites)
        k = np.random.random_integers(0, high=len(probabilites) - 1, size=None)
        upsilon = np.random.uniform(low=0.0, high=prob_max, size=1)

    return k



if __name__ == '__main__':
    probabilites = np.array([0.1, 0.3, 0.1, 0.5])

    outcomes = []
    for i in xrange(100):
        outcomes.append(reject_sampling_finite(probabilites))

    print np.histogram(outcomes, bins=4, range=None, normed=False, weights=None, density=None)
