
def has_cycle(head: Node) -> bool:
    tortoise = head
    hare = head
    while hare and hare.successor:
        hare = hare.successor.successor
        tortoise = tortoise.successor
        if hare == tortoise:
            return True
    return False
