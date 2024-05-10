
def detect_cycle(head):
    if not head:
        return False
    
    slow, fast = head, head
    
    while fast and fast.successor:
        slow = slow.successor
        fast = fast.successor.successor
        
        if slow == fast:
            return True
    
    return False
