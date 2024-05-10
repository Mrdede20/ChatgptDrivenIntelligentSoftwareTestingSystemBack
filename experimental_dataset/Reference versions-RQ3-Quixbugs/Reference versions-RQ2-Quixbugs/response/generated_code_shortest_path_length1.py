Code 1:

```
import math
from fibheap import *

def shortest_path_length(graph, startnode, goalnode):
    heap = makefheap()
    distances = {startnode: 0}
    insert_or_update = heap.insert

    for node in graph:
        if node != startnode:
            distances[node] = math.inf
        insert_or_update((distances[node], node))

    while heap.total_nodes():
        dist, node = heap.extract_min()
        if node == goalnode:
            return dist
        for successor, successor_distance in graph[node].items():
            new_distance = dist + successor_distance
            if new_distance < distances[successor]:
                distances[successor] = new_distance
                insert_or_update((new_distance, successor))

    return None

```

Code 2:

```
import math
from fibheap import *

def shortest_path_length(graph, startnode, goalnode):
    heap = makefheap()
    distances = {startnode: 0}
    get = heap.get
    insert_or_update = heap.insert_or_update

    for node in graph:
        if node != startnode:
            distances[node] = math.inf
        insert_or_update((distances[node], node))

    while heap:
        dist, node = heap.pop_min()
        if node == goalnode:
            return dist
        for successor, successor_distance in graph[node].items():
            new_distance = dist + successor_distance
            if new_distance < distances.get(successor, math.inf):
                distances[successor] = new_distance
                insert_or_update((new_distance, successor))

    return None
```