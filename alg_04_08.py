##------------------------------------------
## 함수 선언부 -----------------------------
##------------------------------------------

#파이썬 노드 클래스 구현
class Node():
    def __init__(self):
        self.data = None
        self.link = None

def printNodes(start):
    current = start
    if current == None:
        return
    print(current.data, end = " ")
    while current.link != None:
        current = current.link
        print(current.data, end = " ")
    print()

def insertNode(findData, insertData):
    global memory, head, current, pre
    # 1. head앞에 넣는경우
    if head.data == findData:
        node = Node()
        node.data = insertData
        node.link = head
        head = node
        memory.append(node)
        return
    #2. 바디에 있는경우
    # 그래도 헤드부터 시작한다
    current = head
    while current.link != None:
        # 현재노드를 이전(pre)노드로 지정
        pre = current
        # 현재노드를 다음노드로 이동
        current = current.link
        if current.data == findData:
            node = Node()
            node.data = insertData
            node.link = current
            pre.link = node
            memory.append(node)
            return
    #3. findData가 없다는 얘기 = 맨뒤에 추가 해야한다.
    node = Node()
    node.data = insertData
    current.link = node
    memory.append(node)
    return

def deleteNode(deleteData):
    global memory, head, current, pre
    # 1. head앞에 넣는경우
    if head.data == deleteData:
        current = head
        head = head.link
        del(current)
        return
    #2. 바디에 있는경우
    # 그래도 헤드부터 시작한다
    current = head
    while current.link != None:
        # 현재노드를 이전(pre)노드로 지정
        pre = current
        # 현재노드를 다음노드로 이동
        current = current.link
        if current.data == deleteData:
            pre.link = current.link
            del(current)
            return

def findNode(findData):
    global memory, head, current, pre
    current = head
    if current.data == findData:
        return current
    while current.link != None:
        # 현재노드를 다음노드로 이동
        current = current.link
        if current.data == findData:
            return current
    return Node()      

##------------------------------------------
## 전역 변수부 -----------------------------
##------------------------------------------
memory = []     
head, current, pre = None, None, None
dataArray = ["다현","정연","쯔위","사나","지효"]


##------------------------------------------
## 메인 코드부 -----------------------------
##------------------------------------------

node = Node()       #첫번째 노드
node.data = dataArray[0]
head = node
memory.append(node)

for data in dataArray[1:]:
    pri = node
    node = Node()
    node.data = data
    pri.link = node
    memory.append(node)

printNodes(head)

insertNode("다현","헤뱅")
insertNode("쯔위","쯔테")
insertNode("구구","테일")

printNodes(head)

print("삭제!!================")

deleteNode("헤뱅")
printNodes(head)
deleteNode("쯔테")
printNodes(head)
deleteNode("테일")
printNodes(head)

print("찾기!!================")

fNode = findNode("없니")
print(fNode.data)