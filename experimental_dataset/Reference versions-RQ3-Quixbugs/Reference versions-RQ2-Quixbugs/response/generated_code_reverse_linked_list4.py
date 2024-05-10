Program 1:

```
def reverse_linked_list(head):
    prev = None
    current = head
    
    while current:
        next_node = current.successor
        current.successor = prev
        prev = current
        current = next_node
        
    return prev
```

Program 2:

```
def reverse_linked_list(head):
    if head.successor is None:
        return head
    
    rest = reverse_linked_list(head.successor)
    head.successor.successor = head
    head.successor = None
    
    return rest
```

Note: Both programs use the same method name `reverse_linked_list` and parameter type of `head` which represents the starting node of the singly-linked list. Program 1 iteratively reverses the linked list by updating the successor pointers of each node. Program 2 uses recursion to reverse the linked list in a similar way by getting the reversed linked list of the rest of the list after head, and setting the successor pointers accordingly.