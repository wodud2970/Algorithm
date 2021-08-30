# 떡의 개수(N)와 요청한 떡의 기리이 (M)을 받기
n , m  = map(int, input().split())
#각 떡의 개별 높이 입력받기
array = list(map(int, input().split()))

#이진탐색을 위한 시작점과 끝점 설정
start =  0
end = max(array)

#이진 탐색 수행(반복적)
result = 0
while (start <= end):
    total = 0
    mid = (start + end) // 2
    for x in array:
        #잘랐을 때의 떡의 양 계산 (자르는 값보다 작으면 자르지 않는다 )
        if x > mid:
            total += x - mid
    if total < m: #total 값이 m 값보다 작으면 더 많이 나와 줘야하므로  end 값을 땡겨주고
        end = mid - 1
    else: #total > m  m값이 total 보다 작을때 result 값을 계산해주고 start 값을 오른쪽으로 땡겨준다  start와 end값이 일치 할때 까지
        result = mid
        start = mid + 1
print(result)