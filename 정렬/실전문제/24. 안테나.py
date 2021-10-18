n = int(input())
lst = list(map(int, input().split()))
lst.sort()
print(lst)
comp = []
for i in range(n):
    sum = 0
    for j in range(n):
        sum += abs(lst[i] - lst[j])

    comp.append(sum)

print(lst[comp.index(min(comp))])
