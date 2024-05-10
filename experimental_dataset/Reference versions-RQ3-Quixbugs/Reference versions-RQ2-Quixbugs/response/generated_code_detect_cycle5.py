Program 1:

```python
def has_cycle(head):
    hare = head
    tortoise = head
    while hare and hare.successor:
        hare = hare.successor.successor
        tortoise = tortoise.successor
        if hare == tortoise:
            return True
    return False
```

Program 2:

```python
def has_cycle(head):
    hare = head
    tortoise = head
    while hare and hare.successor:
        hare = hare.successor
        if hare == tortoise:
            return True
        hare = hare.successor
        if hare == tortoise:
            return True
        tortoise = tortoise.successor
    return False
```

Both programs use Floyd's cycle-finding algorithm to detect whether a linked list has a cycle or not. The first program uses two pointers, hare and tortoise, and moves the hare pointer twice as fast as the tortoise pointer. The second program also uses two pointers, but moves the hare pointer one step at a time, making two checks for equality with the tortoise pointer in each iteration of the loop.