# """Tests for queue to make sure it is last in - first out."""


# import pytest

# INIT_TEST = [
#     [None],
#     [1],
#     ["hello world"],
#     [[1, 2, 3]],
#     [(5, 3)],
#     [-3],
#     [[5, 'hi', [3, 5, None]]],
#     [[]],
#     [''],
#     []
# ]


# @pytest.fixture(scope='module', params=INIT_TEST)
# def q(request):
#     """Create a instance of our Queue."""
#     from queue import Queue
#     return Queue()


# def test_init_none():
#     from queue import Queue
#     my_queue = Queue()
#     assert isinstance(my_queue, Queue)


# @pytest.mark.parametrize('input', INIT_TEST)
# def test_enqueue(q, input):
#     """Test enqueue method to make sure tail is set to the end of the queue."""
#     q.enqueue(input)
#     assert q.tail.data is input


# @pytest.mark.parametrize('input', INIT_TEST)
# def test_enqueue_2(q, input):
#     """Test enqueue method to make sure that the new node is connected to the queue."""
#     old_tail = q.tail
#     q.enqueue(input)
#     assert q.tail.prev is old_tail


# @pytest.mark.parametrize('input', INIT_TEST)
# def test_enqueue_3(q, input):
#     """Test enqueue method to make sure the queue connects to the tail."""
#     q.enqueue(input)
#     assert q.tail.prev.next.data is input


# def test_dequeue(q):
#     """Test pop method to make sure it removes the node at the head and returns the value inside."""
#     old_head_data = q.head.data
#     assert q.dequeue() is old_head_data


# def test_dequeue2():
#     """Test that dequeueing from an empty queue raises error."""
#     from queue import Queue
#     my_q = Queue()
#     with pytest.raises(AttributeError):
#         my_q.dequeue()


# def test_size(q):
#     """Test size method to make sure it returns the correct number of nodes in the queue."""
#     size_number = q.size()
#     print('Size is: ', size_number)
#     cur = q.head
#     for num in range(size_number):
#         if cur != q.tail:
#             cur = cur.next
#     assert cur == q.tail

# def test_size_change(q):
#     """Test that dequeue changes size."""
#     size_number = q.size()
#     q.dequeue()
#     assert q.size() == size_number - 1


# def test_peek(q):
#     """Test that peek returns the correct value."""
#     assert q.peek() == q.head.data
