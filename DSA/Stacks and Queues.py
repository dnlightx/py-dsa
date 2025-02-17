# Stacks -> LIFO
x = []
print(x)

# Appending to the top -> O(1)
x.append(4)

x.append(3)
x.append(7)
x.append(9)
print(x)


# Popping -> O(1)
x.pop()
print(x)

# Accesing the top element (last in the case of stacks) -> O(1)
print(x[-1])

# Is stack empty? -> O(1)
if x:
    print(True)


# Queues -> FIFO
from collections import deque
q = deque()
print(q)

# Enqueue -  Appending to the end -> O(1)
q.append(4)
q.append(6)
print(q)


# Dequeue - popping the first element -> O(1)
q.popleft()
print(q)

# Accesing the top element (first in the case of queues) -> O(1)
print(q[0])

# Accesing the bottom element (last in the case of queues) -> O(1)
print(q[-1])