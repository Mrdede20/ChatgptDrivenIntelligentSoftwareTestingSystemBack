
def reverse_linked_list(head):
    node_list = []
    current_node = head

    while current_node:
        node_list.append(current_node)
        current_node = current_node.successor

    for i in range(len(node_list)-1, 0, -1):
        node_list[i].successor = node_list[i-1]

    node_list[0].successor = None

    return node_list[-1]
