
def detect_cycle(head):
    if not head:
        return False
    
    slow, fast = head, head.successor
    
    while fast is not None:
        if fast == slow:
            return True
        
        slow = slow.successor
        if fast.successor is not None:
            fast = fast.successor.successor
        else:
            break
    
    return False
