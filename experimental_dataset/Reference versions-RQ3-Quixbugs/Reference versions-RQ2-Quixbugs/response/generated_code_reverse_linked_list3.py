Program 1:

```
def reverse_linked_list(head):
    prev_node = None
    current_node = head

    while current_node:
        next_node = current_node.successor
        current_node.successor = prev_node
        prev_node = current_node
        current_node = next_node

    return prev_node
```

Program 2:

```
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
```

Note: Both programs share the same method name and parameter type as described in the prompt.