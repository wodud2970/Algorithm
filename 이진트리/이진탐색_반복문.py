def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        # 찾은 경우 중간점 인덱스 변환
        if array[mid] == target: #존재하지않으면 array[mid] 값이 target 값과 같지 않다
            return mid
        #중간점의 값보다 찾고자 하는 값이 적은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

# n (원소의 개수) 가 target (찾고자 하는 문자열)을 입력받기
n, target = map(int, input().split())
array = list(map(int, input().split()))

#이진 탐색 수행 결과 출력
result = binary_search(array, target, 0, n -1 ) #0부터 시작 하므로 -1
if result == None:
    print('원소가 존재하지 않음')
else:
    print(result + 1)

#내일 이진코드 재귀랑 반복구현해보기