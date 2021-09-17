#보드 정보
n = int(input())
#뱀 방향 위치
k = int(input())

#맵의 정보
data = [[0] * (n+1) for _ in range(n+1)] #맵정보
info = []

#맵 정보(사과 있는 곳은 1로 표시)
for _ in range(k):
    a, b = map(int, input().split())
    data[a][b] = 1

#방향 회전 정보 입력
l = int(input())
for _ in range(l):
    x, c = input().split()
    info.append((int(x), c))

#처음에는 오른쪽을 보고 있으므로 (동 남 서 북)
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]

#처음 direction == 0
def turn(direction, c):
    if c == 'L':
        direction = (direction - 1 ) % 4
    else :
        direction = (direction + 1 ) % 4
    return direction

def simulate():
    x, y = 1, 1 #뱀의 머리위치
    data[x][y] = 2 # 뱀이 존재하는 위치는 2로 표시
    direction = 0 #처음에는 동쪽을 보고 있음
    time = 0 #시작한 뒤에 지난 '초' 시간
    index = 0 #다음에 회전할 정보
    q = [(x,y)] #뱀이 차지하고 있는 위치 정보 *꼬리가 앞쪽) #원래의 위치
    while True:
        #위치를 한칸 이동
        nx = x + dx[direction]
        ny = y + dy[direction]
        #맵 범위 안에 있고 뱀의 몸통이 없는 위치 라면 #이동후 조건을 씌워줌
        if 1 <= nx and nx <= n and 1 <= ny and ny <= n and data[nx][ny] != 2:
            #사과가 없다면 이동후에 꼬리 제거
            if data[nx][ny] == 0:
                data[nx][ny] = 2 #몸통을 나둔다
                q.append((nx,ny))
                px, py =q.pop(0) #원래 있던 정보 삭제
            #사과가 있다면 이동후 꼬리 그대로두기 꼬리를 두고 가는거구나..이거 둬서 머하냐 근데
            if data[nx][ny] == 1:
                data[nx][ny] = 2 #지나갔던 길에 몸통을 둔다
                q.append((nx, ny))
        #벽이나 뱀의 몸통과 부딪혔다면
        else:
            time += 1 #시간만 늘려주고 종료
            break
        x, y = nx, ny #다음위치로 머리를 이동
        time += 1
        if index < 1 and time == info[index][0]: #회전일 시간이면 회전 #index = 0 info안에 정보가 없을때 사용해준다
            direction = turn(direction, info[index][1])
            index += 1
    return time

print(simulate())
