from collections import deque
n, m  = map(int, input().split())
lst = list(map(int, input().split()))
count =0
deq = deque(lst)

for i in range(n-1):
    k = deq.popleft()
    for j in deq:
        if k != j:
            count += 1


print(count)