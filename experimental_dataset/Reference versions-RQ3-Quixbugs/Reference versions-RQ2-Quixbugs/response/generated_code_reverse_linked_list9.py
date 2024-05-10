Here are two implementations of the reverse_linked_list() function, both of which use the Node class you provided and follow the algorithm you described:

Implementation 1:

```
def reverse_linked_list(head):
    node = head
    prevnode = None
    while node is not None:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node
        node = nextnode
    return prevnode
```

In this implementation, we start at the head of the linked list and use a while loop to iterate through each node in the list. For each node, we save its successor node in a temporary variable nextnode, set its successor pointer to the previous node (which will be None for the first node), and update prevnode to be the current node. We then move on to the next node in the list until there are no more nodes. Finally, we return the new head of the reversed list, which will be the last node we visited (now pointing to None).

Implementation 2:

```
def reverse_linked_list(head):
    if head is None or head.successor is None:
        return head
    prevnode = None
    node = head
    while node is not None:
        nextnode = node.successor
        node.successor = prevnode
        prevnode = node
        node = nextnode
    return prevnode
```

In this implementation, we check if the input head node is None or has no successor (meaning it is the only node in the list), and if so, we simply return the head as is. Otherwise, we follow the same algorithm as in Implementation 1 to reverse the list.