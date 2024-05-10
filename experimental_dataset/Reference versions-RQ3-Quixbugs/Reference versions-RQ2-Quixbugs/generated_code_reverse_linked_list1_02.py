
def reverse_linked_list(head):
    if head.successor is None:
        return head
    new_head = reverse_linked_list(head.successor)
    head.successor.successor = head
    head.successor = None
    return new_head
