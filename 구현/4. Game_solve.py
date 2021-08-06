# N x M 직사각형 / 욱지 or 바다  /캐릭터는 동서남북
# 맵의 칸 (A,B)로 나타내고 A는 북쪽으로 떨어진 칸의 개수 B는 서쪽으로부터 떨어진 칸
# 캐릭터 상하좌우 바다는 갈 수없다

# 1.  현재 방향 기준 왼쪽 방햐으로 간다
# 2. 왼쪽 방향 가보지 않았다면  왼쪽 회전 한ㄴ칸 전진 #왼쪽방향에 가보지 않는 칸이 없다면회전만
# 3. 네 방향 보두 가봤으면  방향을 본상태로 뒤로 1칸 가고 1단계로 간다  뒤에가 바다이면 움직일 수없다

#방향이 들어가니까 어렵다
#Map
n,m =  list(map(int,input().split()))

#캐릭터
x,y,z =list(map(int,input().split()))
dx = [-1,1,0,0]             #[0,0,-1,1]
dy = [0,0,-1,1] # L R U D   #[1,-1,0,0]
move = ['북','남','서','동'] # 북  -북(남)  dx <->dy(서) , -dx -dy(동)

#방향

#맵
maps = []
for i in range(n):
    maps.append(list(map(int,input().split())))
num = 0
#행동
while True:
    print('시작')
    # 왼쪽으로 돌기
    if z == 0:
        z = 3
    else:
        z -= 1
    #위치에 방향에 따라 가는곳
    if z == 0 :
        dx = [-1,1,0,0]
        dy = [0,0,-1,1]
    elif z== 1:
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
    elif z == 2:
        dx =[1,-1,0,0]
        dy =[0,0,1,-1]
    else:
        dx = [0,0,-1,1]
        dy = [-1,1,0,0]
    #0 이면
    try:
        if maps[x + dx[2]][y + dy[2]] == 0:
            nx = x + dx[2]
            ny = y + dy[2]

            map[x][y]= 1
            x,y = nx, ny
            num += 1
        else:
            continue
    except:
        continue
    k =0
    for i in maps:
        if [1,1,1,1] == i:
            k += 1
        if k ==4:
            break

print(num)


k = sum([[1,2,3],[2,3,4]])
print(k)


