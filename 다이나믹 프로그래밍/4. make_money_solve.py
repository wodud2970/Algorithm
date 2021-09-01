n, m = map(int, input().split())

array = [int(input()) for _ in range(n)]

d = [0] * 1000

for i in array:
    d[i] = 1




if d[m] == 0:
    print(-1)
else:
    print(d[m])