n,k = map(int, input().split())

a = sorted(list(map(int, input().split())) ) # 1 2 3 4 5
b = sorted(list(map(int, input().split())), reverse=True) # 6 6 5 5 5
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]


print(sum(a))
