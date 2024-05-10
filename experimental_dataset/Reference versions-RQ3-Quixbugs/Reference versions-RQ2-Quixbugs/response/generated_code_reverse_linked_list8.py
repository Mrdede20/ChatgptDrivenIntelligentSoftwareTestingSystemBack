Here are the two programs to reverse a linked list:

Program 1:

```
def reverse_linked_list(node):
    prev_node = None
    current_node = node
    while current_node:
        next_node = current_node.successor
        current_node.successor = prev_node
        prev_node = current_node
        current_node = next_node
    return prev_node
```

Program 2:

```
def reverse_linked_list(node):
    if not node or not node.successor:
        return node
    new_head = reverse_linked_list(node.successor)
    node.successor.successor = node
    node.successor = None
    return new_head
```

Both programs achieve the same intention of reversing a linked list. The first program uses an iterative approach with two pointers to reverse the linked list, whereas the second program uses a recursive approach to reverse the linked list.