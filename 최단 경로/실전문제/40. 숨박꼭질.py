# N개의 헛간
# 1번 헛간으로 부터 최단 거리가 가장 먼 헛간이 가장 안전하다
import heapq
import sys
# input = sys.stdin.readlines()
INF = int(1e9)

#노드의 개수 및 간선의 개수를 입력받기
n, m = map(int, input().split())

# 시작 노드를 1번 헛간으로 설정
start = 1

#각 노드에 연결되어 있느 노드에 대한 정보를 담는 리스트를 만들기
graph = [[] for i in range(n + 1)]
#최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1) #최단경로 등록순
#모든 간선 정보를 입력받기
for _ in range(m):
    a, b = map(int, input().split())
    # a번 노드와 b 번 노드의 이동 비용이 1이라는 의미(양방향)
    graph[a].append((b, 1))
    graph[b].append((a, 1))
print(graph)
def dijkstra(start):
    q = []
    # 시작 노드로 가기 위한 최단 경로는 0으로 설정하여, 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q :
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        # 현재 노드가 이미 처리된 적이 있는 노드라면 무시
        if distance[now] < dist: #지금 저장된 거리 < 현재 최단 거리
            continue
        # 현재 노드와 연ㄴ결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1]
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) #더 짧을경우 다시 넣어준다

#다익스트라 알고리즘 수행
dijkstra(start)

#최단 거리가 가장 먼 노드 번호(동빈이가 숨을 헛간의 번호)
max_node = 0
#도달할 수 있는 노드 중에서 최단거리가 가장 먼 노드와의 최단거리
max_distance = 0
#최단 거리가 가장 먼 노드와의 최단 거리와 동일한 최단 거리를 가지는 노드들의 리스트
result = []

for i in range(1, n+1):
    if max_distance < distance[i]: #최고 먼거리를 확인해준다 (노드번호 저장, 최장거리 저장)
        max_node = i
        max_distance = distance[i]
        result = [max_node]
    elif max_distance == distance[i]: #같으면은 저장
        result.append(i)

print(max_node, max_distance, len(result))

