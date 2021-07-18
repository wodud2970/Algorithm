'''
N이 1이 될 때까지 다 다음의 두 과정 중 하나를 반복적으로 수행하려고한다
단 두 번 째 연산은 N이 K로 나누어떨어질 때만 선택할 수 있다.

1. N에서 1을 뺀다
2. N을 K로 나눈다

'''
import time
n, k  = map(int, input().split())
start = time.time()
answer = 0

while True:
    if n == 1:
        break
    if n % k ==0 :
        n = n // k
    else:
        n -= 1
    answer += 1

print(answer)
print("내가 푼 문제 :", start - time.time())


