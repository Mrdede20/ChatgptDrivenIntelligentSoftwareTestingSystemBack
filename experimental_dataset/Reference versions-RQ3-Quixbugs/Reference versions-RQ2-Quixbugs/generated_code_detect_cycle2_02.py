
def detect_cycle(node):
    tortoise = node
    hare = node.successor
    
    while hare is not None and hare.successor is not None:
        if tortoise == hare:
            return True
        
        tortoise = tortoise.successor
        hare = hare.successor.successor
    
    return False
