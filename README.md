# data-structures

[![Build Status](https://travis-ci.org/AveryPratt/data-structures.svg?branch=bst_remove)](https://travis-ci.org/AveryPratt/data-structures)

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
