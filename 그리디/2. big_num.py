#큰수의 법칙
n, m, k = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

answer = 0
for i in range(m):
    if k == 0:
        answer += second
        k = 3
    else:
        answer += first
    k -= 1


print(answer)

## 정답 1번
n, m, k = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]

result = 0

while True:
    for i in range(k):
        if m == 0 :
            break
        result += first
        m -= 1
    if m  == 0:
        break
    result += second
    m -= 1
print(result)