from collections import deque
# n개의 도시와 m개의 도로
# x는 출발도시 k거리정보
n, m, k, x = map(int, input().split())

graph = [[] for _ in range(n+1)] #도시를 순서로 표현

#그래프 삽입
for _  in range(m):
    a, b = map(int, input().split())
    graph[a].append(b)

#모든 도시에 대한 최단 거리 초기화
distance = [-1] * (n + 1)
distance[x] = 0 #출발 도시까지의 거리는 0으로 설정   (출발도시설정)

#너비 우선 탐색(BFS) 수행
q = deque([x])
while q :
    now = q.popleft()
    #현재 도시에서 이동할 수 있는 모든 도시를 확인
    for next_node in graph[now]:
        #아직 방문하지 않은 도시라면
        if distance[next_node] == -1:
            #최단 거리 갱신
            distance[next_node] = distance[now] + 1
            q.append(next_node)

#최단 거리가 K인 도시의 번호를 오름차순으로 출력
check = False
#출력순서로 하는 거구만
for i in range(1, n+1):
    if distance[i] == k:
        print(i)
        check = True
print(distance)

num = 0
for i in distance:
    if i == k:
        print(num)
    num += 1
#만약 최단 거리가 K인 도시가 없다면, -1 출력
if check == False :
    print(-1)
