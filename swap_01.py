array = [7,5,9,0,3,1,6,2,4,8]

print(array)
for i in range(len(array)):
    min_index = i       #가장 작은 원소의 인덱스
    for k in range(i+1, len(array)):
        if array[min_index] > array[k]:
            min_index = k
    array[i], array[min_index] = array[min_index], array[i]     #스왑
    print(array)

print(array)