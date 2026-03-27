def stringify(node):
    result = ""
    while node:
        result += f"{node.data} -> "
        node = node.next
    return result + "None"