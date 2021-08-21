katok = ['다현', '정현', '쯔위', '사나', '지효', '모모']

# 삭제함수
def delete_data(position):
    kLen = len(katok)
    katok[position] = None

    for i in range(position+1, kLen):
        katok[i-1] = katok[i]       #이동처리
        katok[i] = None             #옴기고 난 후속처리 = 비우기

    del(katok[kLen-1])

print(katok)
delete_data(1)
print(katok)
delete_data(3)
print(katok)