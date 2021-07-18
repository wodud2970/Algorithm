#큰수의 법칙
#배열의 크기 N, 숫자가 더해지는 횟수 M , 그리고 K가 주어질 때 큰수의 법의 결과를 출력
n, m, k = map(int,input().split())
data = list(map(int, input().split()))
data.sort()
first = data[n-1]
second = data[n-2]
k_ = k
answer = 0
for i in range(m):
    if k_ == 0:
        answer += second
        k_ = k
    else:
        answer += first
    k_ -= 1


print(answer)
