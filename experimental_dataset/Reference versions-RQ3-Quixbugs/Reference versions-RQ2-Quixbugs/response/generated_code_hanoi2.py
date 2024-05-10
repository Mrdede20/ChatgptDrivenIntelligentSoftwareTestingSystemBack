Here are two programs that achieve this intention:

Program 1:

```python
def hanoi(height, start, end, middle):
    if height == 0:
        return []
    else:
        moves = hanoi(height - 1, start, middle, end)
        moves.append((start, end))
        moves += hanoi(height - 1, middle, end, start)
        return moves
```
Program 2:

```python
def hanoi(height, start, end, middle):
    if height == 0:
        return []
    else:
        return (hanoi(height-1,start,middle,end) + 
               [(start,end)] + 
               hanoi(height-1,middle,end,start))
```

Both programs take in the height of the initial stack, the starting peg, and the ending peg as arguments, and then return a list of tuples representing the sequence of moves required to solve the puzzle. The difference between the two programs is in the way they concatenate the moves from the recursive calls. 

In program 1, the moves from the recursive calls are first calculated and then appended with the current move to get the final list of moves.

In program 2, the moves from the recursive calls are concatenated directly with the current move to get the final list of moves. This is achieved using Python's ability to concatenate lists with the `+` operator.