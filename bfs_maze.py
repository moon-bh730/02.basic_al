from collections import deque

# bfs 소스코드 구현
def bfs(x, y):
    # queue 구현을 위해deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #queue가 빌때 까지 반복
    while queue:
        x, y = queue.popleft()
        #현재 위치에서 4방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 범위를 벗어난 경우 무시 처리
            if nx < 0 or nx >= n or ny < 0 or ny >= m:
                continue
            #벽인 경우 무시
            if graph[nx][ny] = 0:
                continue
            # 해당 노드를 처음 방문하는 경우만 최단거리 기록
            if graph[nx][ny] == 1:
                graph[nx][ny] = graph[x][y] + 1
                queue.append((nx, ny))
    # 가장 오른쪽 아래까지의 최단 거리 반환
    return graph[n-1][m-1]    


#------------------------------------------------
# 소스 코드부
#------------------------------------------------

# n, m을 공백 기준으로 구분하여 입력
n, m = map(int, input().split())

#2차원 리스트 맵 정보 입력 받기
graph = []
for i in range(n):
    graph.append(lise(map(int, input().split())))

#이동할 4방향 정의(상 하 좌 우)
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#bfs를 수행한 결과 출력
print(bfs(0, 0))