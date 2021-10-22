#전투력이 높은 병사가 앞쪽으로  , 특정 위치에 병사를 열외시키는 방법 , 병사의 수가 최대
n = int(input())
max_value = 0
sol = list(map(int, input().split()))
array = []
result = 0
for i in range(1,n):
        if sol[i-1] < sol[i]:
                result += 1

print(result)

