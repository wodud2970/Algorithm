# target 값을 설정 한다 #이해가 안되....
n = int(input())
data = list(map(int, input().split()))
data.sort()

target = 1
for x in data:
    #만들 수 없는 금액을 찾았을 때 반복 종료
    if target < x:
        break
    print(target, x)
    target += x

# 1 2 3 5


#만들수 없는 금액 출력
print(target)