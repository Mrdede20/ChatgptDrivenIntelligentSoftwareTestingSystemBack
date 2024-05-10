Here are two programs to reverse a singly linked list using the given `Node` class:

**Program 1:**

```python
def reverse_linked_list(head):
    prev = None
    current = head
    while current is not None:
        next_node = current.successor
        current.successor = prev
        prev = current
        current = next_node
    return prev
```

**Program 2:**

```python
def reverse_linked_list(head):
    if head.successor is None:
        return head
    new_head = reverse_linked_list(head.successor)
    head.successor.successor = head
    head.successor = None
    return new_head
```

Both of these programs take in the head node of the singly linked list and iterate through all the nodes. The first program iteratively reverses the direction of the successor pointers of each node, while the second program recursively calls itself to reverse the linked list. Both programs return the new head of the reversed linked list.