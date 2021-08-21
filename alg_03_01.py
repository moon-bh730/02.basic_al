katok = []          # 빈배열

def add_data(friend):       # 새친구 추가 함수
    katok.append(None)
    kLen = len(katok)-1
    katok[kLen] = friend

add_data("다현")
add_data("정현")
add_data("쯔위")
add_data("사나")
add_data("지효")

print(katok)