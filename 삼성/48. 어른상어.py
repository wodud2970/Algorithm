#어른상어 더더 어려운 문제 내 뇌로는 이해도 못하겠다
#시뮬레이션 구현문제
n, m, k = map(int, input().split())

#모든 상어의 위치와 방향 정보를 포함하는 2차원 리스트
array = []
for i in range(n):
    array.append(list(map(int, input().split())))

#모든 상어의 현재 방향 정보
directions = list(map(int, input().split()))

#각 위치마다 특정 냄새의 상어 번호, 특정 냄새의 남은 시간을 저장하는 2차원 리스트
smell = [[[0,0]] * n for _ in range(n)] #map에다가 냄새정보를 뿌린다

#각 상어의 회전 방향 우선순위 정보
priorities = [[] for _ in range(m)]
for i in range(m):
    for j in range(4):
        priorities[i].append(list(map(int, input().split())))

#특정위치에서 이동 가능한 4가지 방향
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

#모든 냄새 정보를 업데이트
#array = 상어 위치 smell 냄새정보
def update_smell():
    #각 위치를 하나씩 확인하며
    for i in range(n):
        for j in range(n):
            #냄새가 존재하는 경우 시간을 1만큼 감소시키기 #냄새가 사라져야하니까
            if smell[i][j][1] > 0:
                smell[i][j][1] -= 1
            #상어가 존재하는 해당 위치의 냄새를 k 로 설정
            if array[i][j] != 0:
                smell[i][j] = [array[i][j], k]
#모든 상어를 이동시키는 함수
def move():
    #이동 결과를 담기 위한 임시 결과 테이블 초기화
    new_array = [[0] * n for _ in range(n)]
    #각 위치를 하나씩 확인하며
    for x in range(n):
        for y in range(n):
            #상어가 존재하는 경우
            if array[x][y] != 0:
                #첫번째 상어, 두번째 상어 위치 정보
                direction = directions[array[x][y] -1] #현재 상어의 방향 ex 4
                found = False
                #일단 냄새가 존재하지 않는 곳이 있는지 확인
                for index in range(4):
                    # 각 상어의 우선 회전정보 첫번째 상어의 우선 정보
                    #다음위치 = 현재 x값 + 이동하는데 우선순위 : 상어의 종류 0 + 방향 4인데 3번쨰 +인덱스 값
                    nx = x + dx[priorities[array[x][y] - 1][direction -1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction -1][index] - 1]
                    if 0 <= nx and nx < n and 0 <= ny and ny < n:
                        if smell[nx][ny][1] == 0:#냄새가 존재하지 않는곳이면
                            #해당 상의 방향 이동 시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] - 1][direction-1][index]
                            #만약 이미 다른 상어가 있다면 번호가 낮은 상어가 들어가도록
                            #상어 이동 시키기
                            if new_array[nx][ny] == 0:
                                new_array[nx][ny] = array[x][y] #new_array에 기존에 상어가 없다면 그냥이동
                            else:
                                new_array[nx][ny] = min(new_array[nx][ny], array[x][y]) #기존에 상어가 있다면 번호가 낮은 상어가 들어가도록
                            found = True
                            break
                if found:
                    continue
                #주변에 모두 냄새가 남아 있다면 자신의 냄새가 있는 곳으로 이동 #냄새가 존재하는곳 밖에 없다면
                for index in range(4):
                    nx = x + dx[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    ny = y + dy[priorities[array[x][y] - 1][direction - 1][index] - 1]
                    if 0 <= nx and n and 0 <= ny and ny < n :
                        if smell[nx][ny][0] ==  array[x][y]: #자신의 냄새가 있는 곳이면 상어랑 냄새위치
                            #해당 상어의 방향 이동시키기
                            directions[array[x][y] - 1] = priorities[array[x][y] -1][direction - 1][index]
                            #상어이동시키기
                            new_array[nx][ny] = array[x][y]
                            break
    return new_array
time = 0
while True:
    update_smell() # 모든 위치의 냄새를 업데이트
    new_array = move() #모든 상어 이동시키기
    array = new_array #맵 업데이트
    time += 1 #시간 증가

    # 1번 상어만 남았는지 체크
    check = True
    for i in range(n):
        for j in range(n):
            if array[i][j] > 1:
                check = False
    if check :
        print(time)
        break

    #1000초가 지날 때 까지 끝나지 않았다면
    if time >= 1000:
        print(-1)
        break