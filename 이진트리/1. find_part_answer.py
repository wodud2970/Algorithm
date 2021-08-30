#이진 탐색으로 푸는법
def bianry_search(array, target, start, end):
    while start <= end:
        mid = start + end //2
        # 찾은 경우 중간점 인덱스로 변환
        if array[mid] == target:
            return mid
        # 중간점의 값보다 찾고자 하는 값이 작은 경우 왼쪽 확인
        elif array[mid] > target:
            end = mid - 1
        # 중간점의 값보다 찾고자 하는 값이 큰 경우 오른쪽 확인
        else:
            start = mid + 1
        return None

# N(가게의 부품 개수) 입력
n = int(input())

#가게에 있는 전체 부품 번호를 공백으로 구분하여 입력
array = list(map(int, input().split()))
array.sort()

#M 손님이 확인 요청한 부품 개수  입력
m = int(input())
# 손님이 확인 요청한 전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x :
    result = bianry_search(array, i, 0, n -1)
    if result != None:
        print('yes', end = ' ')
    else :
        print('no', end = ' ')

# 정렬로 문제 풀기

#N을 입력받기
n = int(input())
array = [0] * 10000001
# 가게에 있는 전체 부품 번호를 입력받아서 기록
for i in input().split():
    array[int(i)] = 1
# M 손님이 확인 요청한 부품개수를 입력받기
m = int(input())
#손님이 확인 요청한 ㅂ전체 부품 번호를 공백으로 구분하여 입력
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부품이 존재하는지 확인
    if array[i] == 1:
        print('yes', end = " ")
    else:
        print('no', end = ' ')

# 집합 자료형으로 이용
# N(가게의 부품 개수)을 입력받기
n = int(input())
#가게에 있는 전체 부품 번호를 입력받아서 집합(set) 자료형에 기록
array = set(map(int, input().split())) #set을해주고 중복 자료형을 없앤다

#M9(손님이 확인 요청한 부품 개수)를 입력받기
m = int(input())
#손님이 확인 요청한 전제 부품 번호를 공백으로 굼분하여 입력
x = list(map(int, input().split()))

#손님이 확인 요청한 부품 번호를 하나씩 확인
for i in x:
    #해당 부품이 존재하는지 확인
    if i in array:
        print('yes', end = ' ')
    else:
        print('no', end = ' ')
