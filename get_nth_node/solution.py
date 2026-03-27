from preloaded import Node

# class Node(object):
#     """Node class for reference"""
#     def __init__(self, data, next=None):
#         self.data = data
#         self.next = next
    
def get_nth(node, index):
    if index < 0:
        raise IndexError()

    if not node:
        raise ValueError()

    for _ in range(index):
        if not node.next:
            raise IndexError()

        node = node.next

    return node
    # Your code goes here.
