# 개선된 다익스타라는 O(ElogV)를 보장한다 V는 노선 개수, E는 간선의 개수를 의미한다 ----> 힙의 자료구조를 사용한다
# 개선된 다익스타라 (데이크스트라)
import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)

#노드의 개수, 간선의 개수를 입력받기
n, m =map(int, input().split())

#시작 노드 번호를 입력받기
start = int(input())

#각 노드에 연결되어 있는 노드에 대한 정보를 담는 리스트 만들기
graph = [[] for i in range(n+1)]

# 최단 거리 테이블을 모두 무한으로 초기화
distance = [INF] * (n+1)

#모든 간선 정보를 입력받기
for _ in range(m):
    a, b, c = map(int, input().split())
    # a번 노드에서 b번 노드로 가는 비용이 c라는 의미 a --c--> b
    graph[a].append((b,c))

#visited가 없다 push 와 pop을 이용하여 삭제해주기 떄문, get_smallest_node가 없다 거리가 최소인것을 찾지 않기 때문에
def dijkstra(start):
    q = []
    # 시작 노드로 가기위한 최단 경로는 0으로 설정하여 q에 삽입
    heapq.heappush(q, (0, start)) #리스트 q에 (0, start)를 넣는다
    distance[start] = 0
    while q: #q가 비어있지 않다면
        #가장 최단 거리가 짧은 노드에 대한 정보 꺼내기
        dist, now = heapq.heappop(q) #(가중치, 노드)
        #현재 노드가 이미 처리된적이 있는 노드라면 무시
        if distance[now] < dist:
            continue
        #현재 노드와 연결된 다른 인접한 노드들을 확인
        for i in graph[now]:
            cost = dist + i[1] #현재 cost값과 정보들의 cost값을 더해준다
            #현재 노드를 거쳐서, 다른 노드로 이동하는 거리가 더 짧은 경우
            if cost < distance[i[0]]: #거쳐서가는 cost 값 < 거치기전 노드 값 비교
                distance[i[0]] = cost
                heapq.heappush(q, (cost, i[0])) #더 작으면 heapq에 push 해준다

dijkstra(start)

#모든 노드로 가기위한 최단거리 출력
for i in range(1, n+1):
    #도달 할수 없는 경우, 무한(INFINITY)라고 출력
    if distance[i] == INF:
        print('INFINITY')
    else:
        print(distance[i])