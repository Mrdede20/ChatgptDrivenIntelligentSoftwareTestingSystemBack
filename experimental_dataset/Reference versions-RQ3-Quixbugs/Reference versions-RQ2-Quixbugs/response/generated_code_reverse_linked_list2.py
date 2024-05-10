Program 1:

```
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
        
def reverse_linked_list(head):
    previous_node = None
    current_node = head
    
    while current_node is not None:
        next_node = current_node.successor
        current_node.successor = previous_node
        previous_node = current_node
        current_node = next_node
        
    return previous_node
```

Program 2:

```
class Node:
    def __init__(self, value=None, successor=None):
        self.value = value
        self.successor = successor
        
def reverse_linked_list(head):
    previous_node = None
    current_node = head
    succs = [current_node]

    while current_node is not None:
        succs.insert(0, current_node)
        current_node = current_node.successor
        
    for i in range(len(succs)):
        if i == 0:
            head = succs[i]
        elif i == len(succs) - 1:
            succs[i].successor = None
        else:
            succs[i].successor = succs[i+1]
    
    return head
```

Note: Both the programs achieve the same purpose of reversing a singly-linked list by manipulating its successor pointers. However, the first program does it by directly manipulating the successor pointers, while the second program utilizes a list to store the nodes in reverse order and then iterates through the list to update the successor pointers.