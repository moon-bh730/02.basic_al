##------------------------------------------
## 함수 선언부 -----------------------------
##------------------------------------------
def isQueueFull():
    global SIZE, queue, front, rear
    if (rear >= SIZE-1):
        return True
    else:
        return False

def isQueueEmpty() :
    global SIZE, queue, front, rear
    if (front == rear) :
        return True
    else :
        return False

def enQueue(data):
    global SIZE, queue, front, rear
    if (isQueueFull()):
        print("queue Ful!!")
        return
    rear += 1
    queue[rear] = data

def deQueue() :
    global SIZE, queue, front, rear
    # 큐가 꽉차면 메시지 출력 후, 그만
    if (isQueueFull()):
        print("queue Ful!!")
        return None
    front += 1
    data = queue[front]
    queue[front] = None
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

enQueue('화사')
enQueue('솔라')
enQueue('문별')
print('<--', queue, '<--')

data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
data = deQueue(); print('디큐 :', data)
print('<--', queue, '<--')