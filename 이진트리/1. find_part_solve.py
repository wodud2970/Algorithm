n= int(input())
is_lst = list(map(int, input().split()))
m = int(input())
check_lst = list(map(int, input().split()))

for i in range(m):
    if check_lst[i] in is_lst:
        print('yes',end=" ")
    else:
        print('no', end= ' ')
