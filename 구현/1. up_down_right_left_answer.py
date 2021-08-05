# N x N 정사각형 , L R U D
# 공간의 크기 N
# L R U D 구현 알고리즘 처음이라 풀지 못했다 다음에는 무조건 푼다

# 행렬 생성
N = int(input())

command = input().split()
x,y =1,1

dx = [0,0,-1,1]
dy = [-1,1,0,0]
move =['L','R','U','D']

# 이동 계획
for plan in command:
    #이동 후 좌표 구하기
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i]
            ny = y + dy[i]
    #공간을 벗어나는 경우 무시
    if nx <1 or ny<1 or nx > N or ny > N:
        continue
    #이동 수행
    x,y = nx,ny

print(x,y)


