"""Implementation of k-means algorithm for grouping clusters of datapoints."""


class KMeans(object):
    """A class for organizing data into clusters based on location and proximity.
    
    fit(self, k=2): iteratively reorganizes data into different clusters until mindiff or maxiter is reached.abs
    predict(self, ):
    """
    def __init__(self, max_iter=5, min_diff=0):
        """Initialize a K-Means Classifier object."""
        self.centroids = []
        self.max_iter = max_iter
        self.min_step = min_step
        self.fitted = False

    def fit(self, data, k=2):
        """Fit K centroids to given data."""
        if k < 0 or k > len(data):
            raise ValueError("K must a positive integer less than the length of data.")
        while not _should_stop(old_centroids, centroids, iteration):
            pass
        self.fitted = True
        pass

    def predict(self, data):
        """Predict the class of given test data after fit."""
        if not self.fitted:
            raise RuntimeError()
        self._classify(data)
        return data

    def _calc_distance(self, pt1, pt2):
        """Calculate the distance between two points."""
        pass

    def _classify(self, data):
        """Assign each datapoint to the nearest centroid."""
        for point in data:
            distances = []
            for cent in self.centroids:
                distances.append(self._calc_distance(cent, point))
            point.group = distances.index(min(distances))

    def _find_mean(self, points):
        """Find the mean coordinates of points."""
        pass

    def _should_stop(self, old_centroids, centroids, iteration):
        """Determine if the fit should stop runnng."""
        pass

    def _assign_centroids(self, data, k):
        groups = []
        for _ in range(k):
            groups.append(data[data["groups"] == k])
        for idx, group in enumerate(groups):
            self.centroids[idx] = self._find_mean(group)
