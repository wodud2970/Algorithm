# 미로
# 괴물  0  괴물 x 1

from collections import deque
n,m = map(int, input().split())

miro = [[int(i) for i in list(input())] for _ in range(n)]

#이동할 네 방향 정의 (상,하,좌,우)
dx = [-1,1,0,0]
dy = [0,0,-1,1]

def bfs(x,y):
    # 큐(Queue) 구현을 위해 deque 라이브러리 사용
    queue = deque()
    queue.append((x,y))
    #큐가 빌 때 까지 반복
    while queue:
        x,y = queue.popleft()
        #현재 위치에서 네 방향으로의 위치 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #미로 찾기 공간을 벗어난 경우 무시
            if nx <0 or ny <0 or nx >= n or ny >= m:
                continue
            #괴물인 경우 무시
            if miro[nx][ny] == 0:
                continue
            #해당 노드를 처음 방문하는 경우에만 최단거리 기록
            if miro[nx][ny] == 1:
                miro[nx][ny] = miro[x][y] + 1
                queue.append((nx,ny))
    return miro[n-1][m-1]

print(bfs(0,0))

for i in range(n):
    for j in range(m):
        #현재위치 0으로
        if miro[i][j] == 1:
            miro[i][j] = 0
