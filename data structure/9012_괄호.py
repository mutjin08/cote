def define(target):
    if len(target)%2!=0:
        return "NO"
    
    stack = 0
    for t in target:
        if t == "(":
            stack += 1
        elif t == ")":
            if stack > 0:
                stack -= 1
            elif stack <= 0:
                return "NO"
    
    if stack > 0:
        return "NO"

    return "YES"

t = int(input())
for _ in range(t):
    target = input()
    print(define(target))