# 단순하게 푸는 예시 (내가 푼게 더 쉬운거 같은데)
# 내가 푼게 더 깔끔한거 같다
import time
n, k = map(int, input().split())
start = time.time()

result = 0

#N이 K 이상이라면 K로 계속 나누기
while n >= k:
    #N이 K로 나누어 떨어지지 않는 다면 1씩빼기
    while n % k != 0:
        n -= 1
        result +=1
    # k로 나누기
    n //= k
    result +=1

#마지막으로 남은 수에 대하여 1씩 빼기

while n > 1:
    n -= 1
    result += 1

print(result)
print("1문제 :", start - time.time())
# 2번째 풀이 N, K를 공백으로 구분하여 입력받기
n, k = map(int, input().split())
start = time.time()

result = 0

while True:
    # (N == K 로 나누어 떨어지는 수)가 될때 까지 1씩 빼기
    #맨처음에 나눈 수를 찾고 그다음에 1의 값을 찾는다
    target = (n//k) *k
    result += (n - target)

    n = target
    #N이 K보다 작을때 (더 이상 나눌 수 없을 때) 반복문 탈출
    if n < k:
        break
    #K로 나누기
    result += 1
    n //= k

#마지막으로 남은 수에 대햐여 1씩 빼기
result += (n-1)
print(result)
print("2문제 :", start - time.time())