import heapq
import sys

input = sys.stdin.readline
INF = (1e9)

#노드의 개수, 간선의 개수, 시작 노드를 입력 받기
n, m, start = map(int, input().split())

#각 누드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

#최단거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기  x --z--> y
for _ in range(m):
    x, y, z = map(int, input().split())
    # x번 노드에서 y번 노드로 가는 비용이 z라는 의미
    graph[x].append((y,z))

def dijkstra(start):
    q = []
    #시작 노드로 가기위한 최단 경로는 0으로 설정하여 , 큐에 삽입
    heapq.heappush(q, (0, start))
    distance[start] = 0
    while q:
        #가장 최단 거리가 짧은 노드에 대한 정보를 꺼내기
        dist, now = heapq.heappop(q)
        #현재 저장된 거리 가중치와 지금 가중치를 비교
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            #현재 노드에서 가중치 + 다른 노드들간의 가중치
            cost = dist + i[1]
            #현재 저장된 가중치와 현재노드 가중치 + 다른 노들와의 관계 가중치 비교
            if cost < distance[i[0]]:
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0]))

#다익스트라 알고리즘을 수행
dijkstra(start)

#도달할 수 있는 노드의 개수
count  = 0
#도달할 수 있는 노드중에서, 가장 멀리 있는 노드와의 최단거리
max_distance = 0
for d in distance:
    #도달할 수 있는 노드의 경우
    if d != INF:
        count += 1
        max_distance = max(max_distance, d)
#시작 노드는 제외해야 하므로 count -1을 출력
print(count -1, max_distance)
