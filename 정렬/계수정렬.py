#특정조건이 부합할 때만 사용하는 알고리즘

#모든 원소의 값이 0보다 크거나 같다고 가정
array = [7, 5, 9, 0, 3, 1, 6, 2, 9, 1, 4, 8, 0, 5, 2]

#모든 범위를 포함하는 리스트 선언(모든 값은 0으로 초기화)
count = [0] * (max(array) +1)

for i in range(len(array)):
    count[array[i]] += 1 #각 데이터에 인덱스 값 증가
print(count)
for i in range(len(count)):
    for j in range(count[i]):
        print(i, end= ' ')

#  시간 복잡도는 O(N + K)
# 퀵 정렬은 일반적인 경우에서 평균적으로 빠르게 동작하기 때문에 데이터의 특성을 파악하기 어렵다면 퀵 정렬을 이용하는것이 유리하다

# 파이썬에서 기본 제공하는 sorted 소스코드
array = [7,5,9,0,3,1,6,2,4,8]

result = sorted(array)
print(result)

array = [7,5,9,0,3,1,6,2,4,8]
array.sort()
print(array)

#정렬 라이브러리에서 key를 활용한 소스코드
array = [('바나나', 2), ('사과',5),('당근',3)]
def setting(data):
    return data[1]
result = sorted(array, key= setting)
print(result)

#파이썬 라이브러리는 병합 정렬과 삽입 정렬의 아이디어를 더한 하이브리드 정렬 알고리즘을 사용하고 있다

# 1. 정렬 라이브러리로 풀 수 있는 문제 , 2. 정렬 알고리즘의 원리에 대해서 물어보는 문제 : 선택, 삽입, 퀵 정렬의 원리를 알고 있다 3. 더 빠른 정렬이 필요한 문제  기존에 알려진 알고리즘의 구젖ㄱ인 개선을 거쳐야 풀 수 있다

