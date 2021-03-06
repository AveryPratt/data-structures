"""Hash table with fixed number of buckets that with different hash functions."""


class HashTable(object):
    """Implement a hash table in Python.

    get(key) - should return the value stored with the given key

    set(key, val) - should store the given val using the given key

    _hash(key) - should hash the key provided (note that this is an
    internal api)
    """

    def __init__(self, buckets, hash_func=None):
        """Create a Hash Table."""
        self.buckets = [[] for n in range(buckets)]
        if hash_func == "xor":
            self._hash = self._xor_hash

    def get(self, key):
        """Should return the value stored with the given key."""
        hash_code = self._hash(key)
        bucket = self.buckets[hash_code]

        for tup in bucket:
            if tup[0] == key:
                return tup[1]

    def set(self, key, val):
        """Should store the given val using the given key.

        If key and val exists in the bucket, remove it to avoid duplicates.
        """
        hash_code = self._hash(key)
        bucket = self.buckets[hash_code]
        if bucket:
            for tup in bucket:
                if tup[0] == key:
                    bucket.remove(tup)
        self.buckets[hash_code].append((key, val))

    def _hash(self, key):
        """Additive hashing function."""
        if type(key) is not str:
            raise TypeError('Hash functions only work on strings.')
        hash_code = sum([ord(letter) for letter in key])
        return hash_code % len(self.buckets)

    def _xor_hash(self, key):
        """Return a hashcode created by the xor operation."""
        if type(key) is not str:
            raise TypeError('Hash functions only work on strings.')
        hash_code = 0
        for char in key:
            hash_code ^= ord(char)
        return hash_code % len(self.buckets)
