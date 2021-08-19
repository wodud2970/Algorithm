# 여담으로 병렬정렬이란것도 있다

# 퀵 정렬 소스코드 기본

array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]
def quick_sort(array, start, end):
    #시작이 끝보다 크거나 같으면 종료
    if start >= end: #원소가 1개이면 종류
        return
    pivot = start
    left = start +1
    right = end
    # 오르쪽 인덱스가 왼쪽 인덱스 크면 (오른쪽 인덱스가 왼쪽 인덱스 보다 작아질 때까지)
    while left <= right:
        #왼쪽에서 피벗 보다 큰 데이터를 찾을 때까지 반복
        while left <= end and array[left] <=array[pivot]: #왼쪽 인덱스는 array 크기보다 작고 왼쪽값이 피봇값보다 작을때 발행
            left += 1
        #오른쪽 에서 피벗 보다 작은 데이터를 찾을 때까지 반복
        while right > start  and array[right] >= array[pivot]:
            right -= 1
        # left와 right가 엇갈렸다면 작은 데이터와 피벗을 교체
        if left > right:
            array[right], array[pivot] = array[pivot], array[right]
        # 엇갈리지 않았다면 왼쪽과 오른쪽 교환
        else:
            array[left] , array[right] = array[right], array[left]
    # 이제 분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬 수행
    quick_sort(array, start, right -1)
    quick_sort(array, right+1, end)

quick_sort(array, 0, len(array) -1) #end 는 index의 끝점
print(array)

#파이썬의 장점을 살린 퀵 정렬 소스코드
array = [5, 7, 9, 0, 3, 1, 6, 2, 4, 8]

def quick_sort(array):
    #리스트가 하나 이하의 원소만을 담고 있다면 종류
    if len(array) <= 1:
        return array

    pivot =array[0]
    tail =array[1:]

    left_side = [x for x in tail if x <= pivot] #분할된 왼쪽부분
    right_side = [x for x in tail if x > pivot] #분할된 오른쪽부분

    #분할 이후 왼쪽 부분과 오른쪽 부분에서 각각 정렬을 수행하고 전체 리스트를 반환
    return quick_sort(left_side) + [pivot] + quick_sort(right_side)

print(quick_sort(array))

#퀵정렬은 O(NlogN)이다  최악의 경우 O(N^2)가 된다