# 지도크기
n, m  = map(int, input().split())

#지도 (초기 지도)
# maps = [list(map(int, input().split())) for _ in range(n)]
maps = []
for _ in range(n):
    maps.append(list(map(int, input().split())))
#벽을 설치한 지도 (초기값)
temp = [[0] * m for _ in range(n)]

# 4가지 이동 방향에 대한 리스트  #위 오른쪽 아래 왼쪽 (시계 방향)
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

result = 0

#모든 경우의 수를 계산해야한다
# DFS와 BFS를 실수없이 구현해야한다

# 1. 벽 3개를 설치를 0에 대해 모든 경우의수를 계산
# 깊이 우선 탐색(DFS)을 이용해 울타리를 설치하면서, 매번 안전 영역의 크기 계산

# 2. 각 바이러스의 위치에서 DFS와 BFS를 수행하여 연결된 모든 부분을 감연시키도록 처리
def virus(x, y):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        # 상 하 좌 우 중에서 바이러스가 퍼질 수 있는 경우
        # 이동값 행이 0보다 크고 맵크기 n보다 작고 이동값 열이 0보다 크고 맵크기 m보다 작고
        if nx >= 0 and nx < n and ny >= 0 and ny < m :
            if temp[nx][ny] == 0:
                # 해당 위치에 바이러스 배치하고 재귀적으로 수행
                temp[nx][ny] = 2
                virus(nx, ny) #퍼진곳에서 또 상하좌우로 퍼지게 만들어주기위해 재귀적으로 수행


# 3. 0으로된 값을 세어주어 가장 max값이 나오도록한다
#현재 맵에서 안적영역의 크기를 계산하는 매서드
def get_score():
    score = 0
    for i in range(n):
        for j in range(m):
            if temp[i][j] == 0:
                score += 1
    return score

def dfs(count):
    global result
    # 울타리가 3개 설치된 경우 (더 이상 울타리를 추가 해주지 않아도 되는 경우)
    if count == 3:
        for i in range(n):
            for j in range(m):
                temp[i][j] = maps[i][j]
        #각 바이러스의 위치에서 전파 진행
        for i in range(n):
            for j in range(m):
                if temp[i][j] == 2:
                    virus(i,j)
        #안전 영역 최댓값 게산
        result = max(result, get_score())
        return
    #빈 공간에 울타리 설치 (3개를 무조건 설치해주어야한다) #모든 경우의수를 확인해준다
    for i in range(n):
        for j in range(m):
            if maps[i][j] == 0:
                maps[i][j] = 1
                count += 1
                dfs(count)
                maps[i][j] = 0
                count -= 1


dfs(0)
print(result)