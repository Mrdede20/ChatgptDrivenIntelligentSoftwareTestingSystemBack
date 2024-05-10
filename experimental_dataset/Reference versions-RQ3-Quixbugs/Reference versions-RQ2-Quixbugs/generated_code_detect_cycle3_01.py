
def detect_cycle(node):
    tortoise = node
    hare = node

    while True:
        if hare.successor is None or hare.successor.successor is None:
            return False

        hare = hare.successor.successor
        tortoise = tortoise.successor

        if hare == tortoise:
            return True
