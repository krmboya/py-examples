from __future__ import print_function

import math
import random

# We have a list of 10 unsorted integers between 1 and 100 inclusive
list_to_sort = [random.randint(1, 100) for i in range(10)]
print("List before sorting: ", list_to_sort)


def heapsort(l):
    """Sort list l using heapsort"""

    # build a max heap in the list so that largest element is first
    heapify(l)
    print("Heapified list", l)

    end = len(l) - 1  # the last index

    while end > 0:
        # swap the largest element to end
        l[end], l[0] = l[0], l[end]

        # heap size reduced by 1
        end -= 1

        # restore the heap property
        # sift down the top item to correct position in heap
        sift_down(l, 0, end)


def heapify(l):
    """Create a max heap out of elements in l"""

    # start at the parent of the last element
    count = len(l)
    start = i_parent(count - 1)

    while start >= 0:
        # sift down node at start so that all nodes below it
        # are in heap order
        sift_down(l, start, count - 1)

        # move to next parent node
        start -= 1


def sift_down(l, start, end):
    """Repair heap who's root element is at start"""

    root = start

    while i_left_child(root) <= end:  # while there's at least one child
        child = i_left_child(root)
        swap = root  #  swap keeps track of node to swap with

        if l[swap] < l[child]:
            # set swap to left child if greater than root
            swap = child

        if (child + 1) <= end and l[swap] < l[child + 1]:
            # if there's a right child
            # and it is greater that root/left child
            # set to swap
            swap = child + 1

        if swap == root:
            # root holds largest element
            # since we assume heaps rooted at children are valid,
            # we're done
            return

        else:
            # swap root into correct position
            l[root], l[swap] = l[swap], l[root]
            root = swap

        print("sifting down", l[root], l)

def i_parent(i):
    """Return index of parent of i in heap"""

    return int(math.floor((i - 1) / 2))

def i_left_child(i):
    """Return left child of element at i"""

    return 2 * i + 1


# Sort the list now
heapsort(list_to_sort)

print("List after sorting", list_to_sort)
