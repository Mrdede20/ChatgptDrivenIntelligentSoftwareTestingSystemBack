
def has_cycle(head):
    hare = tortoise = head
    while hare and hare.successor:
        hare = hare.successor.successor
        tortoise = tortoise.successor
        if hare == tortoise:
            return True
    return False
