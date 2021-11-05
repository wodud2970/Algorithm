n,m,s = map(int,input().split())

graph = [[] for _ in range(n+1)]
for i in range(m):
    x,y = map(int,input().split())
    graph[x].append(y)
graph = [sorted(i)  for i in graph]
print(graph)
visited = [False] * (n+1)
#재귀적인 dfs
def dfs(graph,v,visited):
    visited[v] =True #같던곳을 -1
    print(v, end=' ')
    for i in graph[v]:
        if not visited[i]:
            dfs(graph, i, visited)

from collections import deque

#stack 을이용한 bfs
def bfs(graph, s, visited):
    queue = deque([s]) #리스트형식으로 시작해서 그렇구만
    visited[s] = True
    while queue:
        v = queue.popleft()
        print(v, end = ' ')
        for i in graph[v]:
            if not visited[i]:
                queue.append(i)
                visited[i] = True


dfs(graph, s, visited)
print()
visited = [False] * (n+1)

bfs(graph, s, visited)

