"""Tests for the K-Means Classifier."""
import pandas as pd
import pytest
import numpy as np

@pytest.fixture
def kmc():
    """Fixture to return a default KMC."""
    from k_means import KMeans
    return KMeans()

@pytest.fixture
def some_data():
    """Fixture to return some dummy data."""
    data = np.array([[2, 3], [4, 5], [6, 7], [8, 9], [1, 1], [2, 2], [3, 3], [4, 4]])
    return pd.DataFrame(data=data)

def test_calc_distance_rows(kmc):
    """Test the _calc_distance method of the K Means Classifier."""
    rows = [[2, 2, 1, 0], [0, 0, 1, 0]]
    data = pd.DataFrame(data=rows, columns=['x', 'y', 'class', 'dummy'])
    assert kmc._calc_distance(data.loc[0], data.loc[1]) == 8 ** .5

def test_calc_distance(kmc):
    """Test distance calculator helper method."""
    assert kmc._calc_distance([0, 0, 0, 0], [3, 4, 0, 0]) == 5.0

def test_find_mean(kmc, some_data):
    """Unit test for find mean."""
    data_means = kmc._find_mean(some_data)
    assert data_means == [3.75, 4.25]

# def test_assign_centroids(kmc, some_data):
#     for item in some_data:
#         pass
#     kmc._assign_centroids(some_data, 10)
#     import pdb; pdb.set_trace()

def test_fit(kmc, some_data):
    """Test that fit applies classifications."""
    kmc.fit(some_data)
    assert kmc.fitted
