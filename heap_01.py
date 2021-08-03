import sys
import heapq
#from typing import Iterable
input = sys.stdin.readline

def heapsort(interable):
    h = []
    result = []
    #모든 원소를 차례로 힙에 삽입
    for value in interable:
        heapq.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

print("-------------array 크기-------------")
n = int(input())
arr = []

for i in range(n):
    print("-------------{}번째-------------".format(i))
    arr.append(int(input()))

res = heapsort(arr)

print("-------------result-------------")

for i in range(n):
    print(res[i])