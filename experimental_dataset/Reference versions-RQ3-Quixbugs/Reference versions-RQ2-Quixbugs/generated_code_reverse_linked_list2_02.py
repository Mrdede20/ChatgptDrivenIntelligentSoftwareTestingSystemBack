
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
        
def reverse_linked_list(head):
    previous_node = None
    current_node = head
    succs = [current_node]

    while current_node is not None:
        succs.insert(0, current_node)
        current_node = current_node.successor
        
    for i in range(len(succs)):
        if i == 0:
            head = succs[i]
        elif i == len(succs) - 1:
            succs[i].successor = None
        else:
            succs[i].successor = succs[i+1]
    
    return head
