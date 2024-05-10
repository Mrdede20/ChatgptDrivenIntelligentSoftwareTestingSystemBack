
def reverse_linked_list(head):
    prevnode = None
    while head:
        nextnode = head.successor
        head.successor = prevnode
        prevnode = head
        head = nextnode
    return prevnode
