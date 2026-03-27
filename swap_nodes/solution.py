from preloaded import Node

def swap_pairs(head):

    if not head:
        return head

    basic_node = Node(head)
    _basic_node = basic_node

    while _basic_node.next and _basic_node.next.next:
        a = _basic_node.next
        b = a.next

        _basic_node.next, a.next, b.next = b, b.next, a
        _basic_node = a

    return basic_node.next
