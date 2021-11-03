#BFS 나 DFS를 섞어야 되는거 같은데...
INF = int(1e9) #무한을 의미하는 값으로 10억을 설정

#노드의 개수, 간선의 개수를 입력 받기
n,m =map(int, input().split())

# 2차원 리스트[그래프 표현]을 만들고, 모든 값을 무한으로 초기화
graph =[[INF] * (n+1) for _ in range(n+1)]

#자기 자신에서 자기 자신으로 가는 비용은 0으로 초기화
for a in range(1, n+1):
    for b in range(1, n+1):
        if a == b:
            graph[a][b] = 0

#각 간선에 대한 정보를 입력받아, 그값으로 초기화
for _ in range(m):
    # A에서 B로 가는 비용을 1로 설정
    a, b = map(int ,input().split())
    graph[a][b] = 1


#점화식에 따라 플로이드 워셜 알고리즘 수행
for k in range(n+1):
    for a in range(n+1):
        for b in range(n+1):
            graph[a][b] = min(graph[a][b], graph[a][k], graph[k][b]) #값이 없는 거는 INF 처리


result = 0
#각 학생을 번호에 따라 한명씩 확인하여 도달 가능한지 체크
for i in range(1, n+1):
    count = 0
    for j in range(1, n+1):
        if graph[i][j] != INF or graph[j][i] != INF:
            count += 1
        if count == n:
            result += 1
print(result)