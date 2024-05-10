
def reverse_linked_list(head):
    if head.successor is None:
        return head
    
    rest = reverse_linked_list(head.successor)
    head.successor.successor = head
    head.successor = None
    
    return rest
