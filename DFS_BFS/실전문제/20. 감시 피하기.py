#선생님 T, 학생 S, 장애물 O
#개 쌉어렵네 바로 정답 간다

#선생의 행열을 다 막아야 하고 그게 선생 위,아래, 왼, 오를 맞춰 줘야한다

#조합으로 푸는 방법
from itertools import combinations

n = int(input()) #복도의 크기
board = [] # 복도 정보( N x N)
teachers = [] # 모든 선생님 위치 정보
spaces = [] #모든 빈 공간 위치 정보

for i in range(n):
    board.append(list(input().split()))
    for j in range(n):
        #선생님이 존재하는 위치 정장
        if board[i][j] == 'T':
            teachers.append((i,j))
        #장애물을 설치할 수 있는 (빈 공간) 위치 저장
        if board[i][j] == 'X':
            spaces.append((i,j))

#특정 방향으로 감시를 진행
def watch(x, y, direction):
    #왼쪽 방향으로 감시
    if direction == 0:
        while y >= 0:
            if board[x][y] == 'S': #학생이 있는 경우
                return True
            if board[x][y] == 'O': #장애물이 있는 경우
                return False
            y -= 1
    #오른쪽 방향으로 감시
    if direction == 1:
        while y < n :
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            y += 1
    # 위쪽 방향으로 감시
    if direction == 2:
        while x >= 0:
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x -= 1

    # 아래쪽으로 감시
    if direction == 3:
        while x < n :
            if board[x][y] == 'S':
                return True
            if board[x][y] == 'O':
                return False
            x += 1
    #아무것도 감시하지 못했을때
    return False
#장애물 설치 이후에 , 한명이라도 학생이 감지 되는지 검사
def process():
    #모든 선생님의 위치를 하나씩 확인
    for x, y in teachers:
        #4가지 방향으로 학생들 감지할 수 있는지 확인
        for i in range(4): #4방향으로 감시
            if watch(x,y,i):
                return True
            return False

find = False #학생이 한명도 감지되지 않도록 설치할수 있는지의 여부

#빈 공간에서 3개를 뽑는 모든 조합을 확인
for data in combinations(spaces, 3):
    #장애물 설치해보기
    for x, y in data:
        board[x][y] = 'O'

    #학생이 한명도 감지되지 않는경우
    if not process():
        #원하는 경우를 발견한 것임(아무도 감시되지 않으면) 즉 process가 False
        find = True
        break
    #설치된 장애물을 다시 없애기
    for x,y in data:
        board[x][y] = 'X'
    #제거 후 다시 설치 해서 반복하여 발견

if find:
    print('YES')
else:
    print("NO")


#DFS로 푸는 방법법--------------------------------------------
from collections import deque
n = int(input())
l = [list(map(int, input().split())) for _ in range(n)]
temp = [['X']* n for _ in range(n)]

def dfs(temp, i, j, dr):
    #위로검사
    if dr == 0:
        while i> 0:
            i -= 1
            if temp[i][j] == 'O':
                return True
            if temp[i][j] == 'S':
                return False
    elif dr == 1:
        while i < n-1:
            i += 1
            if temp[i][j] == 'O':
                return True
            if temp[i][j] == 'S':
                return False

    elif dr == 2:
        #왼쪽으로 검사
        while 0<j:
            j -= 1
            if temp[i][j] == 'O':
                return True
            if temp[i][j] == 'S':
                return False
    else:
        #오른쪽으로 검사
        while j<n-1:
            j += 1
            if temp[i][j] == 'O':
                return True
            if temp[i][j] == 'S':
                return False

def process(temp):
    for i in range(n):
        for j in range(n):
            if temp[i][j] == 'T':
                for b in range(4):
                    if dfs(temp, i, j, b) == False:
                        #학생 발경
                        return False
    return True

flag = False

def casedfs(count):
    global flag, temp , l #flag 찾는지여부, 시도 temp, 맵 l
    if flag == 1:
        return 1
    #3개이면 process를 실행하여 막을 수 있는 경우와 아닌경우를 찾아준다
    if count == 3:
        for i in range(n):
            for j in range(n):
                temp[i][j] = l[i][j]
        if process(temp) == True:
            #막을 수 있는 경우
            flag = True
            return
    else:
        for i in range(n):
            for j in range(n):
                if l[i][j] == 'X':
                    l[i][j] == 'O'
                    count += 1
                    casedfs(count)
                    count -= 1
                    l[i][j] = 'X'
casedfs(0)

if flag == True:
    print('Yes')
else:
    print('No')
