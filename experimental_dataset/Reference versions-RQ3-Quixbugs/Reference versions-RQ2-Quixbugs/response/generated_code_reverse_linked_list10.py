Here are two programs that achieve the intention:

Program 1:

```
def reverse_linked_list(head):
    prevnode = None
    curnode = head
    while curnode != None:
        nextnode = curnode.successor
        curnode.successor = prevnode
        prevnode = curnode
        curnode = nextnode
    return prevnode
```

Program 2:

```
def reverse_linked_list(head):
    prevnode = None
    curnode = head
    while curnode.successor != None:
        nextnode = curnode.successor
        curnode.successor = prevnode
        prevnode = curnode
        curnode = nextnode
    curnode.successor = prevnode
    return curnode
```

Both programs use the same method name and parameter type (`reverse_linked_list(head)`), as requested. The first program uses a `while` loop to iterate through each node in the list, while the second program checks for a `None` value in the `successor` field to determine when to stop iterating. Both programs swap the `successor` pointer with a `prevnode` variable to effectively reverse the order of the list. The loop continues until all nodes have been reversed, and the function mutates the list by changing the `successor` pointers of each node. The second program additionally handles the case where the head of the list is the only node in the list.