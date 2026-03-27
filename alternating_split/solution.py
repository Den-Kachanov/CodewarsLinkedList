class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, first, second):
        self.first = first
        self.second = second

def alternating_split(head):
    if not head or not head.next:
        raise Exception("Error")

    a = head
    b = head.next

    first = a
    second = b

    while b and b.next:
        a.next = b.next
        a = a.next

        b.next = a.next
        b = b.next

    a.next = None
    if b:
        b.next = None

    return Context(first, second)