
def reverse_linked_list(head):
    prevnode = None
    curnode = head
    while curnode.successor != None:
        nextnode = curnode.successor
        curnode.successor = prevnode
        prevnode = curnode
        curnode = nextnode
    curnode.successor = prevnode
    return curnode
