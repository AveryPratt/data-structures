# data-structures

This repository contains sample code for several classic data structures in Python.

## Linked List:
A singly-linked list containing nodes that all stem from the head.
methods:
- push(val)
    adds a node containing val to the head of the list.
- pop()
    removes the node at the head of the list and returns the value.
- size()
    returns the number of nodes on the stack.
- search(val)
    returns the closest node to the head of the list that contains val.
- remove(node)
    removes node from the list.
- display()
    returns a string displaying the contents of the list in the format of a tuple.

## Stack (composed from linked list):
A data structure with basic first-in: first-out functionality
methods:
- push(val)
    adds a node containing val to the top of the stack
- pop()
    removes and returns the value at the top of the stack

## Double Linked List:
A doubly-linked list containing nodes that point to the nodes before and after them.
methods:
- push(val)
    adds a node containing val to the head of the list.
- append(val)
    adds a node containing val to the tail of the list.
- pop()
    removes the node at the head of the list and returns the value.
- shift()
    removes the node at the tail of the list and returns the value.
- search(val)
    returns the closest node to the head of the list that contains val.
- remove(val)
    removes the node containing val closest to the head from the list.
Use-cases:
        A double-linked list would be more appropriate than a single-linked list if the list was bing used
    as a way to store and retrieve data. In that use-case the abiliry to navigate up and down the list in order to find data would be necessary. A single-linked list would be more appropriate than a double-linked list if the user was intnded to only have one chance to access the node and then move on. A use-case like this would probably be simmilar to an online test where the user couldn't change answers once they had been submited.


## Queue
A first-in first-out linear data structure
methods:
- enqueue()
    adds an item to the end of the queue.
- dequeue()
    removes an item from the front of the queue.
- size()
    returns the number of items in the queue.
- peak()
    returns the value of the first item in the queue without removing it.
Use-cases:
        A queue is a good tool for keeping track of requests that cannot be processed immediately. They can also be used in pairs to form a stack.


Developed by Avery Pratt, Patrick Saunders, and Joey DeRosa