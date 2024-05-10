
def reverse_linked_list(head):
    prevnode = None
    curnode = head
    while curnode != None:
        nextnode = curnode.successor
        curnode.successor = prevnode
        prevnode = curnode
        curnode = nextnode
    return prevnode
