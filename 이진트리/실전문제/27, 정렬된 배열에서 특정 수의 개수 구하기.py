length, n = map(int, input().split())
lst = list(map(int, input().split()))

#count를 이용해서 푸는 거
count = lst.count(n)
if count == 0:
    print(-1)
else:
    print(count)

result = 0
#이진트리를 이용하여 푸는방법
for i in lst:
    if i == n:
        result += 1

if result == 0:
    print(-1)
else:
    print(result)