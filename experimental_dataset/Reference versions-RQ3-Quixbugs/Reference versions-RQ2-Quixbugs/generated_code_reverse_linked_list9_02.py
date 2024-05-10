
def reverse_linked_list(head):
    if head is None or head.successor is None:
        return head
    prevnode = None
    node = head
    while node is not None:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node
        node = nextnode
    return prevnode
