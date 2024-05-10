
def reverse_linked_list(head):
    node = head
    prevnode = None
    while node is not None:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node
        node = nextnode
    return prevnode
