#노드와 간선
n, m  = map(int, input().split())

INF = (1e9)



graph = [[INF]*(n+1) for _ in range(n+1)]


#자기 노드값 0으로 만들기
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b = map(int, input().split())
    graph[a][b] = 1
    graph[b][a] = 1  #양방향이라서 이것도 설정 해주어야한다

x, k = map(int, input().split())

for k in range(1, n+1):
   for a in range(1, n+1):
       for b in range(1, n+1):
           graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

# 1 ---> 4 ----> 5
distance = graph[1][k] + graph[k][x]
if distance > INF:
    print(-1)
else:
    print(distance)

