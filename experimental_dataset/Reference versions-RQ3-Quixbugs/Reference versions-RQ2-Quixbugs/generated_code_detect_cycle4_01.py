
def has_cycle(head):
    slow = head
    fast = head
    while fast and fast.successor:
        slow = slow.successor
        fast = fast.successor.successor
        if slow == fast:
            return True
    return False
