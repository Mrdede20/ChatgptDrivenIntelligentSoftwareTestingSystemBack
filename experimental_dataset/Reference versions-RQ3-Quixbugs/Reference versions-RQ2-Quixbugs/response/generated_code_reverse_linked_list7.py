Sure! Here are two programs that achieve the same intention:

Program 1:

```
def reverse_linked_list(head):
    prevnode = None
    node = head
    
    while node is not None:
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
    node = head
    
    while node:
        nextnode = node.successor or None
        node.successor, prevnode, node = prevnode, node, nextnode
    
    return prevnode
```

Both programs take in the head node of a singly linked list and reverse the direction of the successor pointers to reverse the list. They use a while loop to iterate through each node of the list, and temporarily store the next node in the `nextnode` variable. Then, the successor pointer of the current node is set to the previous node (i.e., the direction is reversed).

In Program 1, the `node` and `prevnode` variables are updated individually with each iteration of the loop. In Program 2, a Python feature called tuple unpacking is used to update all three variables in one statement.