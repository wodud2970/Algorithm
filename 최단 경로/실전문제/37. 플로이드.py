#출발도시
n = int(input())
#도착도시
m = int(input())

# 간선 정보 플루워셜 알고리즘
INF = int(1e9)
graph = [[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아 그값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용은 C라고 설정
    a, b, c = map(int, input().split())
    #가장 짤은 간선 정보만 저장
    if c < graph[a][b]:
        graph[a][b] = c

#점화식에 따라 프로이드 워셜 알고리즘을 수행
#전체행확인해보기
for k in range(1, n+1):
    #값 최소 값 선정
    for a in range(1, n+1):
        for b in range(1, n+1):
            graph[a][b] = min(graph[a][b], graph[a][k] + graph[k][b])

print(graph)



for i in range(n+1):
    for j in range(n+1):
        if graph[i][j] < 1e9:
            print(graph[i][j], end=' ')
    print()