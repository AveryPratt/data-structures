"""Implementation of k-nearest neighbors algorithm for grouping clusters of datapoints."""


import operator


class KNearestNeighbors(object):
    """A class for organizing data into clusters based on the points it is closest to.

    predict(self, data):
    Classifies new data based on the classes of the neighbors nearest to it.
    """

    def __init__(self, data, k=5):
        """Initialize a KNearestNeighbors Classifier object."""
        self.data = data
        self.k = k

    def predict(self, point):
        """Predict the class of given test data based on it's nearest k neighbors."""
        nearest = []
        groups = {}
        for neighbor in self.data:
            dst = self._calc_distance(point, neighbor)
            nearest.append(dst)
            nearest.sort()
            nearest = nearest[:self.k]
        for place in nearest:
            if not groups[place[1]]:
                groups[place[1]] = 0
            groups[place[1]] += 1
        return max(groups.iteritems(), key=operator.itemgetter(1))[0]

    def _calc_distance(self, pt1, pt2):
        """Calculate the distance between two points."""
        dist = 0.0
        for dim in range(len(pt1) - 2):
            dist += (pt1[dim] - pt2[dim]) ** 2
        return dist ** .5
