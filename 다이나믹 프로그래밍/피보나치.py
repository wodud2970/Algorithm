#피보나치 함수
def fibo(x):
    if x == 1 or x == 2:
        return 1
    return fibo(x - 1) + fibo(x - 2)

print(fibo(4))

#빅오 표기법을 사용하면 O(2^n)의 지수시간이 소요된다
#큰 문제를 작은문제로 나눌 수 있다
#작은 무제에서 구한 정답은 그것을 포함하는 큰 문제에서도 동일하다  메모제이션 -> 다이나믹 프로그래밍을 구현하는 방법

#피보나치 함수 (재귀적)

#한 번 계산된 결과를 메모제이션하기위한 리스트 초기화
d = [0] * 100 #메모를 해놔서 중복으로 수행하는것을 방지하는것

#피보나치 함수를 재귀함수로 구현(탑다운 다이나믹 프로그래밍)
def fibo(x):
    #종료조건 ( 1 or 2 일때 1을 반환)
    if x == 1 or x == 2:
        return 1
    #이미 계산한적 있는 문제라면 그대로 반환
    if d[x] != 0:
        return d[x]
    #아직 계산하지 않는 문제라면 점화식에 따라서 피보나치 결과를 반환
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

print(fibo(4))
#O(2^N) 이 O(n)으로 바뀐다

#호출되는 함수를 확인
d = [0] * 100

def pibo(x):
    print('f(' + str(x) +')', end = ' ')
    if x == 1 or x == 2:
        return 1
    if d[x] != 0:
        return d[x]
    d[x] = pibo(x-1) + pibo(x-2)
    return d[x]
pibo(6)
#큰문제를 해결하기위해 작은 문제를 호출한다고 하여 탑다운 방식이라고 한다

#피보나치 수열(반복적)

# 앞서 계산된 결과를 저장하기위한 DP 테이블 초기화
d = [0] * 100

#첫 번째 피보나치 수와 두 번째 피보나치 수는 1
d[1] = 1
d[2] = 1
n = 6

#피보나치 함수 반복문으로 구현(보텀업 다이나믹 프로그래밍) 난 이방법으로 많이 풀었다 
for i in range(3, n+1):
    d[i] = d[i-1] + d[i-2]

print(d[n])