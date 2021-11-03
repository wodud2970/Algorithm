# 3차원 좌표 최소 연결거리
#정사영 시켜서 2개의 좌표로 만들고 할까..?
#같은 평면에 있는 것도 있네..
import math
n = int(input())
lst = [list(map(float, input().split())) for _ in range(n)]
result = [int(1e9)] * n
for i in range(n):
    for j in range(i+1,n):
        a1, b1, c1 = lst[i]
        a2, b2, c2 = lst[j]
        min_num = min(result)
        min_num = min(min_num,int(math.sqrt( (a1 - a2)**2 + (b1-b2)**2 + (c1 - c2)**2 )))
        if min_num not in result:
            max_num = max(result)
            result[result.index(max_num)] =  int(min_num)

print(result)
