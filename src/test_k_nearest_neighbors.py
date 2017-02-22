"""Tests for the K-Means Classifier."""
import pandas as pd
import pytest
import numpy as np

@pytest.fixture
def knn():
    """Fixture to return a k nearest neighbors classifier object built with a pandas dataframe."""
    from k_nearest_neighbors import KNearestNeighbors
    data = np.array([[2, 3], [4, 5], [6, 7], [8, 9], [1, 1], [2, 2], [3, 3], [4, 4]])
    return KNearestNeighbors(pd.DataFrame(data=data))
