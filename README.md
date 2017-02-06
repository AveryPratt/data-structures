# data-structures

[![Build Status](https://travis-ci.org/AveryPratt/data-structures.svg?branch=merge_sort)](https://travis-ci.org/AveryPratt/data-structures) [![Coverage Status](https://coveralls.io/repos/github/AveryPratt/data-structures/badge.svg?branch=merge_sort)](https://coveralls.io/github/AveryPratt/data-structures?branch=merge_sort)

This repository contains sample code for several classic data structures in Python.

## Linked List:
A singly-linked list containing nodes that all stem from the head.
methods:
- **push(val)**
    adds a node containing val to the head of the list.
- **pop()**
    removes the node at the head of the list and returns the value.
- **size()**
    returns the number of nodes on the stack.
- **search(val)**
    returns the closest node to the head of the list that contains val.
- **remove(node)**
    removes node from the list.
- **display()**
    returns a string displaying the contents of the list in the format of a tuple.

## Stack (composed from linked list):
A data structure with basic first-in: first-out functionality
methods:
- **push(val)**
    adds a node containing val to the top of the stack
- **pop()**
    removes and returns the value at the top of the stack

## Double Linked List:
A doubly-linked list containing nodes that point to the nodes before and after them.
methods:
- **push(val)**
    adds a node containing val to the head of the list.
- **append(val)**
    adds a node containing val to the tail of the list.
- **pop()**
    removes the node at the head of the list and returns the value.
- **shift()**
    removes the node at the tail of the list and returns the value.
- **search(val)**
    returns the closest node to the head of the list that contains val.
- **remove(val)**
    removes the node containing val closest to the head from the list.
  Use-cases:
      A double-linked list would be more appropriate than a single-linked list if the list was bing used
    as a way to store and retrieve data. In that use-case the abiliry to navigate up and down the list in order to find data would be necessary. A single-linked list would be more appropriate than a double-linked list if the user was intnded to only have one chance to access the node and then move on. A use-case like this would probably be simmilar to an online test where the user couldn't change answers once they had been submited.

## Queue:
A queue containing nodes that can be added to the end of the list and removed from the front.
methods:
- **enqueue(val)**
    add a node containing val to the end of the que.
- **dequeue()**
    removes a node from the front of the queue and return the value.
- **size()**
    returns the number of nodes in the queue.
- **peek()**
    returns the value of the head withoud dequeueing it.

Developed by Avery Pratt, Patrick Saunders, Joey DeRosa, and Casey O'Kane


## Binary Search Tree:

**Module:** binary_serach_tree.py

**Tests:** test_binary_search_tree.py

**Resources Used:** 
https://codefellows.github.io/sea-python-401d5/assignments/bst_1.html
http://www.growingwiththeweb.com/2015/11/check-if-a-binary-tree-is-balanced.html
https://en.wikipedia.org/wiki/Binary_search_tree

Binary Search Tree supports the following methods:

- **insert(self, val)** 
    will insert the value val into the BST. If val is already present, it will be ignored.
- **remove(self, val)** 
    will remove the node containing the value val from the BST. If val is not in the tree, nothing will happen.
- **search(self, val)**
    will return the node containing that value, else None
- **size(self)**
    will return the integer size of the BST (equal to the total number of values stored in the tree). It will return 0 if the tree is empty.
- **depth(self)**
    will return an integer representing the total number of levels in the tree. If there is one value, the depth should be 1, if two values it will be 2, if three values it may be 2 or three, depending, etc.
- **contains(self, val)**
    will return True if val is in the BST, False if not.
- **balance(self)**
    will return an integer, positive or negative that represents how well balanced the tree is. Trees which are higher on the left than the right should return a positive value, trees which are higher on the right than the left should return a negative value. An ideally-balanced tree should return 0.


## Hash Table:

**Module:** hash_table.py

**Tests:** test_hash_table.py

**Resources Used:** 
http://www.eternallyconfuzzled.com/tuts/algorithms/jsw_tut_hashing.aspx
https://codefellows.github.io/sea-python-401d5/assignments/hash_table.html
https://en.wikipedia.org/wiki/Hash_tree

Hash table supports the following methods:

- get(key) - should return the value stored with the given key, O(n)
- set(key, val) - should store the given val using the given key, O(1) time
- _hash(key) - should hash the key provided (note that this is an internal api)


## Trie:

**Module:** trie.py

**Tests:** test_trie.py

**Resources Used:** 
[http://cs.nyu.edu/~kshitij/courses/ds12/index_files/notes-trie.txt](http://cs.nyu.edu/~kshitij/courses/ds12/index_files/notes-trie.txt)
[https://codefellows.github.io/sea-python-401d5/lectures/trie.html](https://codefellows.github.io/sea-python-401d5/lectures/trie.html)

Trie supports the following methods:

- **insert(self, val)**
  creates a new branch containing nodes that spell the value which diverges where the spelling differs from an existing branch, O(n)
- **contains(self, val)**
  returns whether or not a value is contained as a branch of the trie, O(1)
- **size(self)**
  returns the number of branches in the tree, O(n * k)
- **remove(self, val)**
  finds the branch that the value is on and removes the nodes that are unique to that branch, O(n)
- **trie.depth_first_traversal(start)**
  returns a generator that performs a full depth-first traversal of the graph beginning at start. The argument “start” should be a string, which may or may not be the beginning of a string or strings contained in the Trie. O(1) to create generator, O(n) to iterate through it.

Sorting Algorithms:

- **insertion_sort(input)**
  Sorts an iterable by inserting one item at a time into place. worst-case: O(n^2) best-case: 0(n)

- **merge_sort(input)**
  Sorts an iterable by recursively dividing it into two piles and merging those piles. worst-case: O(n + log(n)) best-case: 0(n + log(n))