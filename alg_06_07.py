##------------------------------------------
## 함수 선언부 -----------------------------
##------------------------------------------
def inStackFull():
    global SIZE, stack, top
    if (top == SIZE-1):
        return True
    else:
        return False

def isStackEmpty():
    global SIZE, stack, top
    if (top == -1):
        return True
    else:
        return False

def push(data):
    global SIZE, stack, top
    if (inStackFull()):
        return
    top += 1
    stack[top] = data

def pop(data):
    global SIZE, stack, top
    if (isStackEmpty()):
        return
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

##------------------------------------------
## 전역변수부  -----------------------------
##------------------------------------------
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


##------------------------------------------
## 메인 코드부 -----------------------------
##------------------------------------------
# stack = ['커피', '녹차', '꿀물', '콜라', '환타']
# top = 4

push("커피1")
push("커피2")
print(stack)

data = pop("커피1")
print(data)
print(stack)