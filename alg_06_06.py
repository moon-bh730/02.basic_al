##------------------------------------------
## 함수 선언부 -----------------------------
##------------------------------------------
def inStackFull():
    global SIZE, stack, top
#    if(top == SIZE-1):
#        return True
#    else:
#        return False
    return (top == (SIZE-1))

def push(data):
    global SIZE, stack, top
    # 스택이 꽉찼으면, 꽉찼다는 메시지 출력하고 종료
    # 아니면, 스택에 데이터 넣기
#    if (top == (SIZE-1)):
#        print("stack full!! insert fail '{}'".format(data))
#    else:
#        top += 1
#        stack[top] = data
#    return    
    if (top == (SIZE-1)):
        print("stack full!! insert fail '{}'".format(data))
        return
    top += 1
    stack[top] = data

def isStackEmpty():
    global SIZE, stack, top
    return top <= -1

def pop():
    global SIZE, stack, top
    # 비엇으면 메시지 후 끝
    if (top <= -1):
        print("stack Empty!!")
        return None
    # 안비었으면 데이터 추출해서 반환
    data = stack[top]
    stack[top] = None
    top -= 1
    return data

##------------------------------------------
## 전역 변수부 -----------------------------
##------------------------------------------
SIZE = 5
stack = [None for _ in range(SIZE)]
top = -1


##------------------------------------------
## 메인 코드부 -----------------------------
##------------------------------------------

#stack = ["커피","녹차","꿀물","콜라","환타"]
#top = 4

#print("스택 풀? ", inStackFull())

push("커피1")
push("커피2")
#push("커피3")
#push("커피4")
#push("커피5")
#push("커피6")

print(stack)
data = pop()
print(data)
data = pop()
print(data)
data = pop()
print(data)
print(stack)