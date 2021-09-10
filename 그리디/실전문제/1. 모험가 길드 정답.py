n = int(input())
data = list(map(int, input().split()))

data.sort() #정렬을 하여 작은것부터 정렬
result = 0 #총 그룹의 수
count = 0 #현재 그룹에 포함된 모험가의수

for i in data: #공포도를 낮은것부터 하나씩확인
    count += 1
    #count ==사람인원 // i는 사람인원보다 더 크거나 같으면 그룹을 증가
    if count >= i: #현재 그룹에 해당 모험가를 포함시키기
        result += 1 #그룹을 증가
        count = 0
print(result)