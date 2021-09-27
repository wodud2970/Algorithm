# 빈칸 0, 집  1, 치킨집 2 ==> 도시의 칸 1부터 시작
# 각각 집은 치킨거리를 가지고 있다 도시의 치킨 거리는 모든 집의 치킨 거리의 합

# n 도시의 정보 m 최대 치킨집
n, m  = map(int, input().split())
#map을 넣어준다
maps = [list(map(int, input().split())) for _ in range(n)]

chicken_house = []
chiken_num = 0
#치킨집 위치를 찾는다
for i in range(n):
    for j in range(n):
        if maps[i][j] == 2:
            # 집을 찾아서 계산해준다
            distance = []
            chiken_num += 1
            for k in range(n):
                for l in range(n):
                    if maps[k][l] == 1:
                        #거리를 계산한 값을 넣어준다
                        num = abs((i+1) - (k+1)) + abs((j+1) - (l+1))
                        distance.append(num)

            chicken_house.append(distance)

print(chicken_house)
#치킨집 갯수 조정
if chiken_num >= m:
    reset_chicken = []
    chicken_idx = 0
    for i in chicken_house:
        reset_chicken.append((sum(i),chicken_idx))
        chicken_idx += 1

    reset_chicken =sorted(reset_chicken, key= lambda x : x[0])
    print(reset_chicken)
    lst = []
    for _,j in reset_chicken[:m]:
        lst.append(chicken_house[j])
    chicken_house = lst

# idx_lst = [x  for _,x in reset_chicken[:m] ]



result_lst = [min(x) for x in chicken_house]
print(sum(result_lst))
print(sum(chicken_house[0]))

#문제 이해를 잘못했다  -->