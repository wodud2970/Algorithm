#도시개수, 통로개수, 도시 C
n, m, c = map(int, input().split())

INF = (1e9)

graph = [[INF] * (n+1) for _ in range(n+1)]

for _ in range(m):
    a, b, k = map(int, input().split())
    graph[a][b] = k

for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0
#결과 출력
count = 0
sum_ = 0
for a in range(1, n+1):
    for b in range(1, n+1):
        if (a == c) and (0 < graph[a][b] < INF):
            sum_ = graph[c][b] if sum_ < graph[c][b] else sum_
            count += 1

print(count, sum_)