"""
Input: line with integer q denoting no of queries, followed by q lines of queries

Each query is in the form:

1 x - Enqueue number x
2   - Dequeue the element at the front
3   - Print the element at the front
"""

import sys

class Queue(object):

    class Node(object):
        def __init__(self, data, next_node):
            self.data = data
            self.next_node = next_node

    def __init__(self):
        self.head = None
        self.tail = None
        

    def enqueue(self, data):
        node = self.Node(data, next_node=None)

        if self.tail:
            self.tail.next_node = node
            self.tail = node

        else:
            # empty queue
            self.head, self.tail = node, node

    def dequeue(self):
        data = None
        if self.head:
            data = self.head.data
            self.head = self.head.next_node
            if not self.head:
                # queue is now empty
                self.tail = None
        return data

    def peek(self):
        """Return value of head"""

        if self.head:
            return self.head.data


queue = Queue()
q = int(sys.stdin.readline().strip())  # no queries to perform
for i in range(q):
    query = sys.stdin.readline().strip().split()
    command = int(query[0])
    if command == 1:
        queue.enqueue(query[1])
    elif command == 2:
        queue.dequeue()
    elif command == 3:
        first_element = queue.peek()
        sys.stdout.write("{0}\n".format(first_element))
        
