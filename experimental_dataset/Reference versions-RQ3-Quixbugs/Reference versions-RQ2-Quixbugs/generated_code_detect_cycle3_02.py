
def detect_cycle(node):
    tortoise = node
    hare = node

    while hare is not None and hare.successor is not None:
        hare = hare.successor.successor
        tortoise = tortoise.successor

        if hare == tortoise:
            return True

    return False
