
# Using Floyd's Algorithm to detect cycle in linked list

def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while True:
        if fast.successor is None or fast.successor.successor is None:
            return False

        slow = slow.successor
        fast = fast.successor.successor

        if slow == fast:
            return True
