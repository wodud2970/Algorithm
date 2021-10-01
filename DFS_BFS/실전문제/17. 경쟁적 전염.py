n, k  = map(int, input().split())
data = [list(map(int, input().split())) for _ in range(n)]
#s 초 (x,y)위치의 값
s, x, y = map(int, input().split())
temp = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        temp[i][j] = data[i][j]

#바이러스 이동방향
dx = [-1,1,0,0]
dy = [0,0,-1,1]
#바이러스 종류
#바이러스가 퍼지게한다
def virus(x,y,kind):
    for i in range(4):
        nx = x + dx[i]
        ny = y + dy[i]
        if nx < n and nx >= 0 and ny >= 0 and ny < n :
            if temp[nx][ny] == 0:
                #해당 위치에 바이러스 배치하고 재귀적으로 수행
                temp[nx][ny] = kind

#다퍼질때까지 가아니라 s가 돌때 까지
#낮은 번호부터 증식한다는 조건을 넣지 안았다  (이거 어캐하지 ..) 이거 조건 안넣어도 성공은 했당...
for _ in range(s):
    #비이러스 종류 확인 후 퍼트리기
    for i in range(n):
        for j in range(n):
            if data[i][j] != 0 :
                virus(i, j, data[i][j])
    data = temp.copy()

print(data[x-1][y-1])