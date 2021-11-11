import math
#에라토스테네스의 체로 풀어보기
m, n = map(int, input().split())


array = [True for i in range(n+1)]
array[1] = 0 #1은 소수가 아님
#
for i in range(2, int(math.sqrt(n) + 1)):
    if array[i] ==True:
        # i를 제외한 i의 모든 배수를 지우기
        j = 2
        while i * j <= n :
            array[i*j] = False
            j += 1

for i in range(m, n+1):
    if array[i]:
        print(array[i])
        print(i)