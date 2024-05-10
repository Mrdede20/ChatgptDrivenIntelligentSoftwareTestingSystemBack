
def detect_cycle(node):
    tortoise = node
    hare = node
    
    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor
        
        if tortoise == hare:
            return True
    
    return False
