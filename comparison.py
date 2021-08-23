from array import array
from random import randint
import time

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

for i in range(len(array)):
    min_index = i
    for k in range(i+1, len(array)):
        if array[min_index] > array[k]:
            min_index = k
    array[i], array[min_index] = array[min_index], array[i]

end_time = time.time()

print("선택정렬 성능 측정 : ", end_time - start_time)

array = []
for _ in range(10000):
    array.append(randint(1,100))

start_time = time.time()

array.sort()

end_time = time.time()

print("기본정렬 성능 측정 : ", end_time - start_time)