food_times = list(map(int, input().split()))
k  = int(input())
result = 0
for i in range(k+1):
    if result == len(food_times):
        result = 0
    #food time이 0 일때는 넘겨주어야한다
    if food_times[result] == 0:
        result += 1
        continue
    food_times[result] -= 1
    result += 1

if result == 3:
    result = 0

print(result + 1)