array = [7, 5, 9, 8, 3, 1, 6, 2, 4, 0]

for i in range(1, len(array)): # 1부터 넣어야지 0과 1 부터 비교를한다
    for j in range(i,0, -1): #인덱스 i부터 1까지 감소하며 반복하는 문법
        if array[j] <array[j-1]: #한 칸씩 왼쪽으로 이동
            array[j] ,array[j-1] =  array[j-1], array[j]
        else:
            break

print(array)
# 반복문 2번사용 O(N^2) 이다  현재 리스트의 데이터가 거의 정렬되어있으면 O(N)의 시간 복잡도를 가진다