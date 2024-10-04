import sys
input = sys.stdin.readline
from collections import deque

n = int(input())
q = deque([])
for _ in range(n):
    command = input().split()
    if len(command) > 1:
        x = command[1]
    command = command[0]

    if command == "push":
        q.append(x)
    elif command == "pop":
        if q:
            print(q.popleft())
        else:
            print(-1)
    elif command == "size":
        print(len(q))
    elif command == "empty":
        if not q:
            print(1)
        else:
            print(0)
    elif command == "front":
        if q:
            print(q[0])
        else:
            print(-1)
    elif command == "back":
        if q:
            print(q[-1])
        else:
            print(-1)