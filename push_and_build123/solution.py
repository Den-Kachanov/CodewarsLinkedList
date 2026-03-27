from preloaded import Node

'''
Node is defined in preloaded like this:

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
'''
    
def push(head, data):
    # Your code goes here.
    res = Node(data)
    res.next = head
    return res

def build_one_two_three():
    # Your code goes here.
    return push(push(push(None, 3), 2), 1)