#개 시발어렵다
from collections import deque
INF = 1e9 #무한을 의미하는 10억을 설정

#맵의 크기 N을 입력받기
n = int(input())

#전체 모든 칸에 대한 정보를 입력
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#아기 상어의 현재 크기 변수와 현재 위치 변수
now_size = 2
now_x, now_y = 0, 0

#아기 상어의 시작 위치를 찾은 뒤에 그 위치엔 아무것도 없다고 처리
for i in range(n):
    for j in range(n):
        if array[i][j] == 9:
            now_x, now_y = i, j
            array[now_x][now_y] = 0
#상어의 이동을 나타내는 array 생성
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

#모든 위치까지의 '최단거리만 계산하는 BFS 함수 (너비 탐색) 함수

def bfs():
    #값이 -1이라면 도달할 수 없다는 의미(초기화)
    dist = [[-1] * n for _ in range(n)]
    # 시작 위치는 도달이 가능하다고 보며 거리는 0
    q = deque([(now_x, now_y)])
    #dist  시작 자리는 0
    dist[now_x][now_y] = 0

    while q:
        x,y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if  0 <= nx < n and 0 <= ny < n :
                #자신의 크기보다 작거나 같은경우에 지나갈수 없음 ( 지날갈수 있는 경우만 조건)
                if dist[nx][ny] == -1 and array[nx][ny] <= now_size:
                    dist[nx][ny] = dist[x][y] + 1 #지나갈수 있으면 dist 값을 +1 해줌
                    q.append((nx,ny)) #다시 스택에 넣어서 반복문
    #모든 위치까지의 최단거리 테이블 반환
    return dist

#최단 거리 테이블이 주어졌을 때 먹을 물고기를 찾는 함수  #최단거리를 찾고 -> 거기서 가장 작은거곳을 간다 (같아도 상관없는듯) 그리고 다시찾고 dist값 바꿔주고
def find(dist):
    x, y = 0,0
    min_dist = INF
    for i in range(n):
        for j in range(n):
            #도달이 가능하면서 먹을 수 있는 물고기 일때
            if dist[i][j] < min_dist:
                x, y = i, j
                min_dist = dist[i][j]
    if min_dist == INF: #먹을수 있는 물고가기 없는 경우 return None
        return None
    else:
        return x, y, min_dist #먹을 물고기의 위치와 최단거리

result = 0 #최종 답안
ate = 0 #현재 크기에서 먹은양

while True:
    #먹을 수 있는 물고기의 위치 찾기
    value = find(bfs())
    #먹을 수 있는 물고기가 없는 경우, 현재까지 움직인 거리 출력
    if value ==None:
        print(result)
        break
    else:
        #현재 위치 갱신 및 이동거리 변경
        now_x, now_y = value[0], value[1]
        result += value[2] #최단거리가 시간
        #먹은 위치에는 이제 아무것도 없도록 처리 (가도되지 않는걸로 처리
        array[now_x][now_y] = 0
        #먹었으니까 증가
        ate += 1
        #자신의 현재 크기 이상으로 먹은 경우, 크기 증가
        if ate >= now_size:
            now_size += 1
            ate = 0




