
def reverse_linked_list(head):
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.successor
        current_node.successor = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node
