""" Node is defined as
class node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
"""


def check_binary_search_tree_(root):
    return node_passes(root, float("-inf"), float("inf"))


def node_passes(node, min_, max_):
    if node is None:
        return True
    return (min_ < node.data < max_ and
            node_passes(node.left, min_, node.data) and
            node_passes(node.right, node.data, max_))
