from collections import deque

stack = deque()

stack.append(5)
stack.append(2)
stack.append(3)
stack.append(4)

print(stack[-1])

h = stack.pop()
print(stack[-1])
print(h)