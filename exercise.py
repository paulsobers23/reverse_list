class Node:
    def __init__(self,data=None, nxt = None):
        self.data = data
        self.next = nxt
    

def reverse(node:Node) -> Node:
    current = node
    prev = None
    nxt = None
    while current:
        nxt = current.next
        current.next = prev
        prev = current
        current = nxt
    return prev
    

