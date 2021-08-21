### 함수 선언부
def add_data(friend):       # 새친구 추가 함수
    katok.append(None)
    kLen = len(katok)-1
    katok[kLen] = friend

# 삭제함수
def delete_data(position):
    kLen = len(katok)
    katok[position] = None
    for i in range(position+1, kLen):
        katok[i-1] = katok[i]       #이동처리
        katok[i] = None             #옴기고 난 후속처리 = 비우기
    del(katok[kLen-1])

# 삽입함수
def insert_data(position, friend):
    katok.append(None)          # 빈칸추가
    kLen = len(katok)-1

    for i in range(kLen, position, -1):
        katok[i] = katok[i-1]       #이동처리
        katok[i-1] = None           #옴기고 난 후속처리 = 비우기

    katok[position] = friend


### 전역 변수부
katok = []
select = -1         # 1. 추가, 2. 삽입, 3. 삭제, 4. 종료

### 메인 코드부
while (select != 4):
    select = int(input("1. 추가, 2. 삽입, 3. 삭제, 4. 종료 >"))

    if (select == 1):
        str_data = input("추가할 데이터 > ")
        add_data(str_data)
        print(katok)
    elif (select == 2):
        int_data = int(input("삽입할 위치 > "))
        str_data = input("추가할 데이터 > ")
        insert_data(int_data, str_data)
        print(katok)
    elif (select == 3):
        int_data = int(input("삭제할 위치 > "))
        delete_data(int_data)
        print(katok)
    elif (select == 4):
        print(katok)
        break
    else:
        print("입력 확인 바랍니다!")
        continue
    