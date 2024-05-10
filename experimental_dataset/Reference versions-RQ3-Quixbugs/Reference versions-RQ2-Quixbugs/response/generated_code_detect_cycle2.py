Here are two programs that achieve the desired task using the Tortoise-Hare algorithm:

Program 1:

```
def detect_cycle(node):
    tortoise = node
    hare = node
    
    while hare is not None and hare.successor is not None:
        tortoise = tortoise.successor
        hare = hare.successor.successor
        
        if tortoise == hare:
            return True
    
    return False
```

Program 2:

```
def detect_cycle(node):
    tortoise = node
    hare = node.successor
    
    while hare is not None and hare.successor is not None:
        if tortoise == hare:
            return True
        
        tortoise = tortoise.successor
        hare = hare.successor.successor
    
    return False
```

Both programs have the same method name and parameter type, and use the Tortoise-Hare algorithm to detect whether a linked list is cyclic or not. The main difference between the two programs is the starting position of the tortoise and hare pointers. Program 1 starts both pointers at the same node, while Program 2 starts the hare pointer at the second node.