
def detect_cycle(head):
    tortoise = head
    hare = head

    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor
        if tortoise == hare:
            return True

    return False
