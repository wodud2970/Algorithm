#집의 개수 (N)와 공유기의 개수(C)를 입력 받기
n, c = list(map(int, input().split()))

#전체 집의 좌표 정보를 받기
array = []
for _ in range(n):
    array.append(int(input()))

array.sort() #이진 탐색을 위해 정렬 수행
start =  array[1] - array[0] #집의 좌표중 가장 작은값 #gap 1
end = array[-1] -array[0] #집의 좌표중에 가장 큰값#gap 8
result = 0
#[1, 2, 4, 8, 9]
while(start <= end):
    mid = (start + end) //2 #mid는 가장 인접한 두 공유기 사이의 거리 gap을 의미 gap 4로 시작
    value = array[0] # 처음 시작 값 1
    count =1 #1개를 이미 설치
    # 현재의 mid값을 이용해 공유기를 설치
    for i in range(1,n) : #앞에서부터 차근차근 설치
        if array[i] >= value + mid : #첫번째 값과 gap 4보다 array가 클때  5
            value = array[i] #처음 시작값이 이동  array i = 8
            count += 1
    #count 2
    if count >= c: #C개 이상의 공유기를 설치할 수 있는 경우, 거리를 증가
        start = mid + 1
        result = mid#최적의 결과를 저장
    else: #C개 이상의 고융기를 설치할 수 없는 경우 거리를 감소 #count가 c보다 작을때 
        end = mid - 1 #end 7

print(result)
