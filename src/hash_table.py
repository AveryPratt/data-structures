"""Contains a hash table with fixed number of buckets that can take different hash functions."""


class HashTable(object):
    """Implement a hash table in Python.

    get(key) - should return the value stored with the given key

    set(key, val) - should store the given val using the given key

    _hash(key) - should hash the key provided (note that this is an
    internal api)
    """

    def __init__(self, buckets, hash_func=None):
        """Create a Hash Table."""
        self.buckets = [[]] * buckets
        if hash_func:
            self._hash = hash_func
        else:
            self._hash = self._additive

    def get(self, key):
        """Should return the value stored with the given key."""
        hash_code = self._hash(key)
        return self.buckets[hash_code]

    def set(self, key, val):
        """Should store the given val using the given key."""
        hash_code = self._hash(key)
        self.buckets[hash_code].append(val)

    def _additive(self, key):
        """Additive hashing function."""
        if type(key) is not str:
            raise TypeError('Hash functions only work on strings.')
        hash_code = sum([ord(letter) for letter in key])
        return hash_code % len(self.buckets)
