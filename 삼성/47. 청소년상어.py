#개 미친 문제 이런거 어캐품 ㅅㅂ
import copy

#4x4 크기의 정사각형에 존재하는 각 물고기의 번호(없으면 01) 방향값을 담는 테이블
array = [[None] * 4 for _ in range(4)]

for i in range(4):
    data = list(map(int, input().split()))
    # 매 줄마다 4마리의 물고리를 하나씩 확인하며
    for j in range(4):
        #각 위치마다 [물고기의 번호, 방향]을 저장 [0,2,4,6,/1,3,5,7] #뒤에 -1은 방향 값이 1부터 시작이라서
        array[i][j] = [data[j*2], data[j*2+1] -1]

#데이터가 어떻게 들어가는지 확인
print(array)

#8가지 방향에 대한 정의
dx = [-1,-1,0,1,1,1,0,-1]
dy = [0, -1, -1, -1, 0, 1, 1, 1]

#현재위치에서 왼쪽으로 회전된 결과를 반환
def turn_left(direction):
    return (direction + 1) % 8

result = 0 #최종결과

#현재 배열에서 특정한 번호의 물고기 위치 찾기
def find_fish(array, index):
    for i in range(4):
        for j in range(4):
            if array[i][j][0] == index:
                return (i,j)
    return None

#모든 물고기를 회전 및 이동시키는 함수
def move_all_fishes(array, now_x, now_y):
    #1번부터 16번까지의 물고기를 차례대로 (낮은 번호부터) 확인
    for i in range(1, 17):
        #해당 물고기의 위치 찾기
        position = find_fish(array, i)
        if position != None: #해당물고기가 없으면
            x, y = position[0], position[1]
            direction = array[x][y][1]
            #해당 물고기의 방향을 왼쪽으로 계속 회전시키며 이동이 가능한지 확인
            for j in range(8):
                nx = x + dx[direction]
                ny = y + dy[direction]
                #해당 방향으로 이동이 가능하다면 이동시키기
                #맵에서 벗어 나지않고
                if 0<=nx and nx < 4 and 0<=ny and ny < 4:
                    #이동했을때 now_x, now_y가 아니면 (즉 같은 자리가 아니면)
                    if not (nx == now_x and ny == now_y):
                        array[x][y][1] = direction #현재 물고기위 방향이 바뀌고
                        array[x][y], array[nx][ny] = array[nx][ny], array[x][y] #자리를 바꾸어준다
                        break #자리를 한번 바꿔기때문에 break
                direction = turn_left(direction) #같은 위치 일때는 방향을 바꾸어준다 8번바뀌면 종료

#상어가 현재 위치에서 먹을 수 있는 모든 물고기의
def get_possible_positions(array, now_x, now_y):
    positions = []
    direction = array[now_x][now_y][1]
    #현재 방향으로 계속이동시키기
    for i in range(4):
        #이게 똑같은 한 방향으로 이동시키는 거구나  1 ~ 4 번 계속 이동 (이동할때마다)
        now_x += dx[direction]
        now_y += dy[direction]
        #범위를 벗어나지 않는지 확인하며
        if 0 <= now_x and now_x < 4 and 0<= now_y and now_y < 4:

            #물고기가 존재하는 경우
            if array[now_x][now_y] != -1:
                positions.append((now_x, now_y))

    return positions

#모든 경우를 탐색하기 위한 DFS 함수ㄹ
def dfs(array, now_x, now_y, total):
    global result
    array = copy.deepcopy(array) #리스트를 통째로 복사 .copy 써도 될텐데
    total += array[now_x][now_y][0] #현재 위치의 물고기 먹기
    array[now_x][now_y][0] = -1 #물고기를 먹었으면 번호 값을  -1로두어 없는 상태로 전환
    move_all_fishes(array, now_x, now_y) #전체 물고기 이동시키기 #이거 적용되나 아마도 전역변수 취급받아서 되긴할듯
    #갈수있는 위치 설정
    positions = get_possible_positions(array, now_x, now_y)

    #이동할 수 있는 위치가 하나도 없다면 종료
    if len(positions) == 0:
        result = max(result, total) #최대 값을 저장 #마지막에 넣어줄려고 놔뒀구나 왜 max쓰지? 그냥 토탈 써도 될텐데
        return
    #모든 이동할 수 있는 위치로 재귀적으로 수행
    for next_x, next_y in positions:
        dfs(array, next_x, next_y, total)

#청소년 상어의 시작 위치(0,0)에서부터 재귀적으로 모든 경우 탐색
dfs(array, 0, 0, 0)
print(result)