Here are the two programs:

Program 1:

```
def reverse_linked_list(head):
    prevnode = None
    node = head
    while node:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node
        node = nextnode
    return prevnode
```

Program 2:

```
def reverse_linked_list(head):
    prevnode = None
    while head:
        nextnode = head.successor
        head.successor = prevnode
        prevnode = head
        head = nextnode
    return prevnode
```

Both programs implement the same algorithm to reverse a singly-linked list. They take the head node of the list as input and return the new head node of the reversed list.

The `while` loop is used to traverse the list and reverse the direction of the successor pointers of each node. The `prevnode` variable is used to keep track of the previous node encountered in the list. Finally, `prevnode` is returned as the new head node of the reversed list.