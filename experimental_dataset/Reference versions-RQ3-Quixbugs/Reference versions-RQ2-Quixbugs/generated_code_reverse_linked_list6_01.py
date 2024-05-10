
def reverse_linked_list(head):
    prevnode = None
    node = head
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node
        node = nextnode
    return prevnode
