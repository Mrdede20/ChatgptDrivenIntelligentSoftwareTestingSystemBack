
def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.successor
        current.successor = prev
        prev = current
        current = next_node
    return prev
