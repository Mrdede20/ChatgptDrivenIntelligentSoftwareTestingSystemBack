
# Using Floyd's Algorithm to detect cycle in linked list

def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.successor is not None:
        slow = slow.successor
        fast = fast.successor.successor

        if slow == fast:
            return True

    return False
