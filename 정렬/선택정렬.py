array = [7, 5, 9, 0, 3, 1, 6, 2, 4, 8]

for i in range(len(array)):
    min_index = i
    for j in range(i+1, len(array)):
        if array[min_index] > array[j]:
            min_index = j
    array[i], array[min_index] = array[min_index], array[i] #스왑

print(array)

#선택 정렬은 N x (N +1) /2 번의 연산을 수행한다  따라서 O(N^2)의 시간복잡도를 가진다
#파이썬의 정렬 알고리즘은 퀵정렬 알고리즘이다 (라이브러리는 기본 c 기반이라 더 빠르다)