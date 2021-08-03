import sys
import heapq
from typing import Iterable
input = sys.stdin.readline

def heapsort(interable):
    h = []
    result = []
    #모든 원소를 차례로 힙에 삽입
    for value in Iterable:
        heaqp.heappush(h,value)
    # 힙에 삽입된 모든 원소를 차례로 꺼내어 담기
    for i in range(len(h)):
        result.append(heapq.heappop(h))
    return result

n = int(input())
arr = []

for i in range():
    arr.append(int(input()))

res = heapsort(arr)

for i in range(n):
    print(res[i])