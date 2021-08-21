katok = ['다현', '정현', '쯔위', '사나', '지효', '모모']

# 삽입함수
def insert_data(position, friend):
    katok.append(None)          # 빈칸추가
    kLen = len(katok)-1

    for i in range(kLen, position, -1):
        katok[i] = katok[i-1]       #이동처리
        katok[i-1] = None           #옴기고 난 후속처리 = 비우기

    katok[position] = friend

print(katok)
insert_data(2, '솔라')
print(katok)
insert_data(7, '문별')
print(katok)