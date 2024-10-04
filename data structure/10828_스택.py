import sys
input = sys.stdin.readline

n = int(input())

stack = []
for _ in range(n):
    target = input().split()

    if len(target)>1:
        x = target[1]
    target = target[0]

    if target == "push":
        stack.append(x)
    elif target == "pop":
        if stack:
            print(stack.pop())
        else:
            print(-1)
    elif target == "size":
        print(len(stack))
    elif target == "empty":
        if not stack:
            print(1)
        else:
            print(0)
    elif target == "top":
        if stack:
            print(stack[-1])
        else:
            print(-1)