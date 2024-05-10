
def has_cycle(head):
    hare = tortoise = head
    while hare and hare.successor:
        hare = hare.successor
        if hare == tortoise:
            return True
        hare = hare.successor
        tortoise = tortoise.successor
    return False
