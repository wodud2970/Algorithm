n, h = map(int, input().split())
array = list(map(int, input().split()))

first_array = [i %h  for i in array]

k =sum(first_array) +  (sum(first_array) // h)

print(k)

#
def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return array[mid]
        elif array[mid] > target :
            end = mid -1
        else:
            start = mid + 1
        return None

