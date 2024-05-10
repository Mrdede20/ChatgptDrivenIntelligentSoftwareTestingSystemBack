Sure, here are two programs that detect if a linked list contains a cycle using Floyd's algorithm:

Program 1:

```
# Using Floyd's Algorithm to detect cycle in linked list

def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while fast is not None and fast.successor is not None:
        slow = slow.successor
        fast = fast.successor.successor

        if slow == fast:
            return True

    return False
```

Program 2:

```
# Using Floyd's Algorithm to detect cycle in linked list

def has_cycle(head):
    if head is None:
        return False

    slow = head
    fast = head

    while True:
        if fast.successor is None or fast.successor.successor is None:
            return False

        slow = slow.successor
        fast = fast.successor.successor

        if slow == fast:
            return True
```

Both programs are implementing the same algorithm with minor differences. The first program checks the condition in the while loop, while the second program checks the condition inside the loop. The second program is more concise but may be harder to read at first.