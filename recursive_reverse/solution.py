class Node(object):
    def __init__(self, data=None):
        self.data = data
        self.next = None

def reverse(head):
    reversed_list = []
    
    if not (head and head.next):
        return head

    while head:
        reversed_list.append(head.data)
        head = head.next


    basic_node = Node(reversed_list[-1])
    _basic_node = basic_node

    for data in reversed(reversed_list[:-1]):
        _basic_node.next = Node(data)
        _basic_node = _basic_node.next

    _basic_node.next = None
    return basic_node