"""Test file for graph.py."""


import pytest


TEST = [
    [1, [1, 2, 3, 4, 5, 6, 7]],
    [2, [2, 5, 6, 3, 7, 1, 4]],
    [3, [3, 7, 1, 2, 4, 5, 6]],
    [7, [7, 1, 2, 3, 4, 5, 6]]
]

TEST_DEPTH = [
    [1, [1, 2, 5, 6, 3, 7, 4]],
    [2, [2, 5, 6, 3, 7, 1, 4]],
    [3, [3, 7, 1, 2, 5, 6, 4]],
    [7, [7, 1, 2, 5, 6, 3, 4]],
]

TEST_WEIGHT = [3, 4, 5, 7, 8, 10, 9, 8]


@pytest.fixture
def g_trav():
    """A more complex graph."""
    from graph import Graph
    g = Graph()
    for i in range(7):
        g.add_node(i + 1)
    g.add_edge(1, 2)
    g.add_edge(1, 3)
    g.add_edge(1, 4)
    g.add_edge(2, 5)
    g.add_edge(2, 6)
    g.add_edge(6, 3)
    g.add_edge(3, 7)
    g.add_edge(7, 1)
    return g


@pytest.fixture
def g_pop():
    """Create a populated instance of the graph."""
    from graph import Graph
    new_g = Graph()
    new_g.add_node('17')
    new_g.add_node('yo')
    new_g.add_node(5)
    new_g.add_edge('17', 'yo')
    new_g.add_edge('yo', 5)
    new_g.add_edge(5, '17')
    return new_g


TEST_LIST = ['17', 'yo', 5]
EDGE_LIST = [('17', ('yo', 2)), ('yo', (5, 6)), (5, ('17', 6))]


@pytest.fixture
def g():
    """Create a new instance of the graph."""
    from graph import Graph
    new_g = Graph()
    return new_g


def test_init(g):
    """Test that the graph was created."""
    assert g.g == {}


def test_nodes_empty(g):
    """Test that nodes returns a list of keys from the dict."""
    assert g.nodes() == []


def test_nodes_populated(g_pop):
    """Test that nodes returns a list of keys from the populated dict."""
    ret = True
    for i in TEST_LIST:
        if i not in g_pop.nodes():
            ret = False
    assert ret


def test_edge(g_pop):
    """Test that edges are made correctly."""
    ret = True
    for i in EDGE_LIST:
        if i not in g_pop.edges():
            ret = False
    assert ret


def test_add_node(g):
    """Test that the add node function works."""
    g.add_node(6)
    assert g.nodes() == [6]


def test_add_edge(g_pop):
    """Test that the edge is added."""
    tst = EDGE_LIST
    g_pop.add_node(0)
    g_pop.add_node('py')
    g_pop.add_edge(0, 'py')
    tst += [(0, 'py'), ('py', 0)]
    ret = True
    for i in EDGE_LIST:
        if i not in tst:
            ret = False
    assert ret


def test_del_node(g_pop):
    """Test that the node is deleted."""
    tst = TEST_LIST
    tst.remove(5)
    g_pop.del_node(5)
    assert 5 not in tst


def test_del_edge(g_pop):
    """Test that the edge is deleted."""
    g_pop.del_edge(5, '17')
    assert (5, '17') not in g_pop.edges()


def test_has_node(g_pop):
    """Test that the node is in the list."""
    g_pop.add_node('in')
    assert 'in' in g_pop.nodes()


def test_neighbors(g_pop):
    """Test that the value is correct for the key."""
    tst = ['17']
    ret = True
    for i in tst:
        if i not in g_pop.neighbors(5):
            ret = False
    assert ret


def test_adjacent(g_pop):
    """Test that adjacent nodes are found."""
    assert g_pop.adjacent('17', 5)

def test_all_edges(g_trav):
    """test all edges."""
    for edges in g_trav.edges():
        assert edges[1][1] in TEST_WEIGHT


@pytest.mark.parametrize('start, answer', TEST_DEPTH)
def test_depth_first_traversal(g_trav, start, answer):
    """Test depth."""
    assert g_trav.depth_first_traversal(start) == answer


@pytest.mark.parametrize('start, answer', TEST)
def test_breadth_first(g_trav, start, answer):
    """Test breadth."""
    assert g_trav.breadth_first_traversal(start) == answer
