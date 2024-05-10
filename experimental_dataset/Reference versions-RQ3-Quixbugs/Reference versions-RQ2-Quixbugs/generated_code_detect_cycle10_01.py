
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
  
def detect_cycle(head):
    tortoise = hare = head
    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor
        if tortoise == hare:
            return True
    return False
