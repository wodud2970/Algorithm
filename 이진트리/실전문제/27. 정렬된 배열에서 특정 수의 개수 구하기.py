#정렬된 수열에서 값이 x인 원소의 개수를 세는 매서드
def count_by_value(array, x):
    #데이터의 개수
    n = len(array)

    # x가 처음 등장한 인덱스 계산
    a = first(array, x, 0, n-1)

    # 수열에 x가 존재하지 않는경우
    if a == None:
        return 0

    # x가 마지막으로 등장한 인덱스 계산
    b = last(array, x, 0, n-1)

    #개수를 반환
    return b - a

#처음 위치를 찾는 이진 탐색 매서드
def first(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    #해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target > array[mid - 1]) and array[mid] == target:
        return mid
    #중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, start, mid - 1)
    #중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

#마지막 위치를 찾는 이진 탐색 메서드
def last(array, target, start, end):
    if start > end:
        return None
    mid = (start + end) // 2

    # 해당 값을 가지는 원소 중에서 가장 왼쪽에 있는 경우에만 인덱스 반환
    if (mid == 0 or target < array[mid + 1]) and array[mid] == target:
        return mid
    # 중간점의 값보다 찾고자 하는 값이 작거나 같은 경우 왼쪽 확인
    elif array[mid] >= target:
        return first(array, start, mid - 1)
    # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
    else:
        return first(array, target, mid + 1, end)

n, x = map(int , input().split())
array = list(map(int, input().split()))

#값이 x인 데이터의 개수 계산
count = count_by_value(array, x)

#값이 x인 원소가 존재하지 않는 다면
if count == 0:
    print(-1)
else:
    print(count)