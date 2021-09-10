n, m  = map(int, input().split())


def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b



parent = [0] * (n+1)
#모든 노드에 대한 진입 차수는 0으로 초기화
indegree = [0] * (n+1)

edges =[]

for _ in range(m):
    a, b, c = map(int, input().split())
    edges.append((a,b,c))

edges.sort(key = lambda x : x[2])
result = 0
#가장 비용이 비싼 길을 없애준다
last = 0


for edge in edges:
    a, b, c = edge
    if find_parent(parent, a) != find_parent(parent, b):
        union_parent(parent, a, b)
        result += c
        last = c

print(result -last)
