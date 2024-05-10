
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
    
def detect_cycle(head):
    if not head:
        return False
    slow = head
    fast = head
    while fast and fast.successor:
        slow = slow.successor
        fast = fast.successor.successor
        if slow == fast:
            return True
    return False
