
def has_cycle(head: Node) -> bool:
    visited = {}
    curr = head
    while curr:
        if curr in visited:
            return True
        visited[curr] = True
        curr = curr.successor
    return False
