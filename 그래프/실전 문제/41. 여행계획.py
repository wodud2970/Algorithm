n, m = map(int, input().split())
parent = [0] * (n+1) #부모 테이블 초기화

# array = [list(map(int, input().split())) for _ in range(n)]

#노드 연결관계를 입력해준다 그리고 집합 관계를 살펴봐준다  (union 연산을 이용해서 서로 연결된 두 노드를 같은 집합에 속하도록 만든다

#특정 원소가 속한 집합을 찾기
def find_parent(parent, x):
    #루트 노드가 아니라면, 루트 노드를 찾을 때 까지 재귀적으로 호출
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

#두 원소가 속한 집합을 합치기
def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

#부모 테이블 상에서, 부모를 자기 자신으로 초기화
for i in range(1, n+1):
    parent[i] = i

#union 연산을 각각 수행
for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: #연결된 경우 union 수행
            union_parent(parent, i+1, j+1)

print(parent)
#여행 계획 입력받기
plan = list(map(int, input().split()))

result = True
#여행 계획에 속하는 모든 노드의 루트가 동일한지 확인
for i in range(m-1):
    if find_parent(parent, plan[i]) != find_parent(parent, plan[i+1]): #부모가 같지 않으면 커트!
        result = False

#여행 계획에 속하는 모든 노드가 서로 연결되어 있는지 ( 루트가 동일한지) 확인
if result:
    print('YES')
else:
    print('NO')