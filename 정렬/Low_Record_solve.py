
n = int(input())
lst = [input().split() for _ in range(n)]

def sort(array):
    return int(array[1])

# for i in sorted(lst, key= lambda x : int(x[1])):
for i in sorted(lst, key=sort):
    print(i[0],end=' ')