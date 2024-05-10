
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
        
def reverse_linked_list(head):
    previous_node = None
    current_node = head
    
    while current_node is not None:
        next_node = current_node.successor
        current_node.successor = previous_node
        previous_node = current_node
        current_node = next_node
        
    return previous_node
