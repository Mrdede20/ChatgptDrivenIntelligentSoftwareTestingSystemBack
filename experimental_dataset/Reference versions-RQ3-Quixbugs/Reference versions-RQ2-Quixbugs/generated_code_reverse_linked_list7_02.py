
def reverse_linked_list(head):
    prevnode = None
    node = head
    
    while node:
        nextnode = node.successor or None
        node.successor, prevnode, node = prevnode, node, nextnode
    
    return prevnode
