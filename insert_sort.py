# 삽입 정렬

array = [7,5,9,0,3,1,6,2,4,8]

print(array)
for i in range(1, len(array)):
    for k in range(i, 0, -1):   #인덱스 i부터 1까지 1씩 감소 반복
        if array[k] < array[k-1]:
            array[k], array[k-1] = array[k-1], array[k]
        else:
            break
    print("{}회 {}".format(i, array))

print(array)