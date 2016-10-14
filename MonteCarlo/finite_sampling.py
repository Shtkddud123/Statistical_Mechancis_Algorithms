# forked
import numpy as np

def reject_sampling_finite(probabilites):
    upsilon = 999
    k = 0
    while upsilon > probabilites[k]:
        prob_max = np.amax(probabilites)
        k = np.random.random_integers(0, high=len(probabilites) - 1, size=None)
        upsilon = np.random.uniform(low=0.0, high=prob_max, size=1)[0]
        print upsilon

    return k

def tower_sampling_finite(probabilites):
    tower = [0]
    for i in range(len(probabilites)):
        tower.append(tower[i] + probabilites[i])

    upsilon = np.random.uniform(low=0.0, high=tower[-1], size=1)[0]

    return binary_search(upsilon, tower)

def binary_search(el, tower):
    min_i = 0
    max_i = len(tower)
    while True:
        index = np.int64((min_i + max_i)*0.5)
        if tower[index] < el:
            min_i = index
        elif tower[index - 1] > el:
            max_i = index
        else:
            return index

if __name__ == '__main__':
    probabilites = np.array([0.1, 0.3, 0.1, 0.5])

    outcomes = []
    for i in xrange(100):
        outcomes.append(tower_sampling_finite(probabilites))

    print np.histogram(outcomes, bins=4, range=None, normed=False, weights=None, density=None)
