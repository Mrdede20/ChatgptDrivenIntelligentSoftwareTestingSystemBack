
def detect_cycle(head):
    node_set = set()
    curr = head

    while curr is not None:
        if curr in node_set:
            return True
        node_set.add(curr)
        curr = curr.successor

    return False
