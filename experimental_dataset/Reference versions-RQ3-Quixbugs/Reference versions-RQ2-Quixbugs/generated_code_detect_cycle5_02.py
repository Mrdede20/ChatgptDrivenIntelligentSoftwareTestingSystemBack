
def has_cycle(head):
    hare = head
    tortoise = head
    while hare and hare.successor:
        hare = hare.successor
        if hare == tortoise:
            return True
        hare = hare.successor
        if hare == tortoise:
            return True
        tortoise = tortoise.successor
    return False
