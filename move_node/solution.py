class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None
    
class Context(object):
    def __init__(self, source, dest):
        self.source = source
        self.dest = dest
    
def move_node(source, dest):
    # Your code goes here.
    # Remember to return the context.
    if not source:
        raise ValueError()

    _dest = Node(source.data)
    _dest.next = dest
    source = source.next

    return Context(source, _dest)