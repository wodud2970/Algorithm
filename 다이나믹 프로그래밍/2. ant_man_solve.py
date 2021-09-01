n = int(input())
array = list(map(int, input().split()))

num = 0
a = 0
b = 0

for i in range(n):
    if i % 2 == 0:
        a += array[i]

    else:
        b += array[i]

    num = max(a,b)

print(num)