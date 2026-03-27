""" For your information:
class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
"""

def sorted_insert(head, data):
    basic_node = Node(data)

    if not head or data < head.data:
        basic_node.next = head
        return basic_node

    current = head

    while current.next and current.next.data < data:
        current = current.next

    basic_node.next = current.next
    current.next = basic_node

    return head