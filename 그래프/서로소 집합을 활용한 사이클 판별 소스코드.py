#간선에 방향성이 없는 무향 그래프에서만 적용이 가능하다

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트노드 찾을 때까지 재귀적으로 호출
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#노드와 간선의 개수를 입력받기
v, e = map(int, input().split())
parent = [0] * (v + 1) #부모 테이블 초기화

#부모 테이블상에서 부모를 자기 자신으로 초기화
for i in range(1, v+1):
    parent[i] = i

cycle = False #사이클 발생여부

for i in range(e):
    a, b = map(int, input().split())
    #사이클이 발생한 경우 종료
    if find_parent(parent,a) == find_parent(parent, b):
        cycle = True
        break
    #사이클이 발생하지 않았다면 union_parent를 실행
    union_parent(parent, a, b)
if cycle:
    print('사이클이 발생했다')
else:
    print('사이클이 발생하지 않았다')
