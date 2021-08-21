stack = [None, None, None, None, None]
top = -1

top += 1
stack[top] = "커피"
top += 1
stack[top] = "녹차"
top += 1
stack[top] = "꿀물"

print(stack)

data = stack[top]
stack[top] = None
top -= 1
print("pop > ", data)
print(stack)

