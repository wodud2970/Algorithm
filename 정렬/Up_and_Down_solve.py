
n = int(input())
lst = [int(input()) for _ in range(n)]

for i in sorted(lst, reverse=True):
    print(i, end = " ")

