n = int(input())
lst = list(map(int, input().split()))
def binary_search(array, start, end):
    #없을겨우
    if start > end:  #이거 설정
        return None
    mid = (start +  end) // 2
    #찾을경우
    if array[mid] == mid: #이거 설정
        return mid
    #타겟이 더 작을 때
    if array[mid] > mid: #클때 작을 target위주로 할거
        return binary_search(array, start ,mid - 1 )
    #타겟이 더 클 클때
    else:
        return binary_search(array, mid +1 , end )


index = binary_search(lst, 0, n-1)
if index == None:
    print(-1)
else:
    print(index)


