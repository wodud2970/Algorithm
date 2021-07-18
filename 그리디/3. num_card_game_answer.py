#각 행마다 가장 작은수를 찾은 뒤 그 수 중에서 가장 큰수
import time
#정답 1 min() 함수를 이용하는 답안 예시
n, m = map(int, input().split())

result = 0

#한 줄 씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    #현재 가장 작은수 찾기
    min_value = min(data)
    #가장 작은수중 큰거 찾기
    result = max(result, min_value)

print(result)

# 2중 반복문 구조를 이용하는 답안제시
n, m = map(int, input().split())
result = 0
#한 줄 씩 입력받아 확인
for i in range(n):
    data = list(map(int,input().split()))
    #현재 줄에서 가장 적은수 찾기
    min_value = 10001
    for a in data: #하나씩 비교해서 찾는건데 이게 의미가 있나 (sort를 사용할 때 사용하는거 같다 )
        min_value = min(min_value, a)
    # 가장 작은수 들 중가장 큰수 찾기
    result = max(result, min_value)

print(result)

