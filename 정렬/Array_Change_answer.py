n, k = map(int, input().split())

a = sorted(list(map(int, input().split())))  # 1 2 3 4 5
b = sorted(list(map(int, input().split())), reverse=True)  # 6 6 5 5 5
for i in range(k):
    if a[i] < b[i]:
        a[i], b[i] = b[i], a[i]
    else:
        break  #첫 번째부터 안되면 더이상 받을게 없으므로 break를 해주어야 한다

print(sum(a))
