#덱 라이브러리는 스택과 큐의 장점을 다 가지고 있다

from collections import deque

queue = deque()

# 요소 추가시 append 뺄때는 popleft를 사용한다.
queue.append(5)
queue.append(2)
queue.append(3)
queue.append(7)
queue.popleft()
queue.append(1)
queue.append(4)
queue.popleft()

print(queue)
queue.reverse()
print(queue)