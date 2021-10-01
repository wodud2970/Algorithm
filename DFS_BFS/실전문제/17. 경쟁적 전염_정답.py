#너비 우선탐색을 이용하여 해결 (낮은 번호부터 증식한다  큐 에 원소를 삽입 해야한다 이후에 너비 우선 탐색을 수행하여 방문하지 않은 위치를 차례대록방문
from collections import deque

n, k = map(int, input().split())

graph = []
data = []

for i in range(n):
    #보드 정보를 하 줄 단위로 입력
    graph.append(list(map(int, input().split())))
    for j in range(n):
        #해당 위치 바이러스가 존재하는 경우
        if graph[i][j] != 0:
            #바이러스 종류, 시간, 위치 x, 위치 y 삽입
            data.append((graph[i][j], 0, i, j))

#정렬 이후에 큐로 옮기기 (낮은 번호의 바이러스가 먼저 증식하므로)
data.sort()
q = deque(data)

target_s, target_x, target_y = map(int, input().split())

#바이러스가 퍼져 나갈수 있는 4가지 위치
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#너비 우선탐색 진행
while q:
    virus, s, x, y = q.popleft()
    #정확히 s초가 지나거나 큐가 빌때 까지 진행
    if s == target_s:
        break
    #현재 노드에서 주변 4가지 위치를 각각 확인
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx >= 0 and nx < n and ny < n and ny >= 0:
            #아직 방문하지않은 위치라면, 그 위치에 바이러스 넣기
            if graph[nx][ny] == 0:
                graph[nx][ny] = virus
                q.append((virus, s+1, nx, ny))

print(graph[target_x -1][target_y -1])
