## 함수
def selectionSort(ary) :
    n = len(ary)
    for i in range(0, n-1):
        minIndex = i
        for k in range(i+1, n) :
            if ary[minIndex] > ary[k] :
                minIndex = k
        ary[i], ary[minIndex] = ary[minIndex], ary[i]
    return ary

## 전역
import random
dataAry = [random.randint(33, 190) for _ in range(20)]

## 메인
print('정렬 전 -->', dataAry)
dataAry = selectionSort(dataAry)
print('정렬 후 -->', dataAry)