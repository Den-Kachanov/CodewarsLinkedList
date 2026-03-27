from preloaded import Node

def linked_list_from_string(s):
    if s == "None":
        return None

    values = s.split(" -> ")
    print(values)
    if values[0] == "None":
        return None
    head = Node(int(values[0]))
    current = head

    for v in values[1:]:
        if v == "None":
            break
        current.next = Node(int(v))
        current = current.next

    return head
