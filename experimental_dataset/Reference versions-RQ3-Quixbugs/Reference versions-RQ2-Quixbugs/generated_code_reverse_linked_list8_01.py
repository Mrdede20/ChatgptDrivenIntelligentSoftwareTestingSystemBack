
def reverse_linked_list(node):
    prev_node = None
    current_node = node
    while current_node:
        next_node = current_node.successor
        current_node.successor = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node
