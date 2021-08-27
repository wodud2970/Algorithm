# 재귀함수로  구현한 인진 탐색하기
n, target = map(int, input().split())
array = list(map(int, input().split()))

def binary_search(array, target, start, end):
    #없을겨우
    if start > end:  #이거 설정
        return None
    mid = end // 2
    #찾을경우
    if array[mid] == target: #이거 설정
        return mid
    #타겟이 더 작을 때
    if array[mid] > target: #클때 작을 target위주로 할거
        return binary_search(array, target, start ,mid)
    #타겟이 더 클 클때
    else:
        return binary_search(array, target, mid +1 , end )
# n-1 조심
result =binary_search(array, target, 0 ,  n -1 ) #조건 넣기

if result == None:
    print('값이 존재하지 않습니다 ')
else:
    print(result + 1) #+1 조심 항상 0부터 인것도 생가가 해야한다


#반복문으로 풀기
def binary_search(array, target, start, end):

    # if start > end: #While 조건식으로 해야함
    #     return None
    while start <= end:
        mid = end //2
        if array[mid] == target:
            return mid
        # 클때
        if array[mid] > target:
            end = mid - 1 # -1 해야함
        # 작을 때
        else:
            start = mid + 1 # +1 해야함
    return None #없을 때 설정해야함

if result == None:
    print('값이 존재하지 않습니다 ')
else:
    print(result + 1) #+1 조심 항상 0부터 인것도 생가가 해야한다


