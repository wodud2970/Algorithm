#소수 2보다 큰 자연수 중에서 1과 자기잔승 ㄹ제외한 자연수로는 나누어 떨어지지 않는 자연수
def is_prime_number(x):
    #2부터 (x-1)까지의 모든수를 확인하면
    for i in range(2,x):
        #x가 해당 수로 나누어 떨어진다면
        if x % i == 0:
            return False
    return True

print(is_prime_number(4))
print(is_prime_number(7))

import math
#소수 판별함수
def ist_prime_number(x):
    # 2부터 x의 제곱근까지의 모든 수를 확인하며
    for i in range(2, int(math.sqrt(x) + 1)):
        # x가 해당수로 나누어 진다면
        if x % i == 0:
            return False
    return True #소수

print(is_prime_number(4))
print(is_prime_number(7))

#에라토스테네스의 채 알고리즘
import math

n = 1000 #2부터 1000까지의 모든 수에 대하여 소수판별
array = [True for i in range(n+1)] #처음엔 모든 수가 소수(True)인 것으로 초기화 (0과 1은 제외)

#에라토스테네스의 채 알고리즘
for i in range(2, int(math.sqrt(n) + 1)): #2부터 젭곱근까지의 모든수를 확인하여
    if array[i] == True:
        #i를 제외한 i의 모든 배수를 지우기
        j = 2 #2의 배수부터 실행하여 계속 올려줌
        while i * j <= n:
            array[i*j] = False
            j += 1

#모든 소수를 출력
for i in range(2, n+1):
    if array[i]:
        print(i, end=' ')

