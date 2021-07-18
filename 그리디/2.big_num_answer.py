import time
## 정답

n, m, k = map(int,input().split())
data = list(map(int, input().split()))
start = time.time()
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
#k가 끝나면 seconde 값을 넣어주고
    if m  == 0:
        break
    result += second
    m -= 1

print(result)
print("첫번째 풀이 시간: ",time.time() - start)
# M의 크기가 100억 이상이면 시간 초과 판정을 받는다
# 정확한 풀이 반복되는 수열을 파악을 하여푼다


n, m, k = map(int, input().split())

data = list(map(int, input().split()))
start = time.time()
data.sort()
first = data[n-1]
second = data[n-2]

#가장 큰수가 더해지는 횟수의 계산
count = int(m/(k+1)) * k  #몫값을 계산
count += m%(k+1) #나머지 값을 더해준다

result = 0
result += count * first #총더해지는 값에 first 값이 더해지는 횟수를 더하고
result += (m - count) * second #총 더해지는 값에 second 값을 횟수를 계산해서 더해준다
print(result)
print("두번째 풀이 시간: ",time.time() - start)


#문제 풀이
'''
5 10000000 3
2 4 5 4 6
57500000
첫번째 풀이 시간:  2.0723235607147217

5 10000000 3
2 4 5 4 6
57500000
두번째 풀이 시간:  0.0
'''