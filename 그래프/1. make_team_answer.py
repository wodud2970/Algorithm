#특정원소가 속한 집합을 찾기
def find_parent(parent, x):
    # 루트 노드가 아니라면, 루트 노드를 찾을때까지 재귀적으로 호출
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

n, m = map(int, input().split())
parent = [0] * (n+1)

for i in range(1, n+1):
    parent[i] = i

# 각연산을 하나씩확인
for i in range(m):
    oper, a, b = map(int, input().split())
    #합집합 연산인 경우
    if oper == 0 :
        union_parent(parent,a,b) #합치는것으로 먼저 바꾸고 팀을 확인!합쳐진 연산후 부모를 찾아서 같은 팀으로 확인하는 것이다
    #찾기 (find) 연산인 경우 /// 같은팀 여부확인
    if oper == 1:
        if find_parent(parent,a) == find_parent(parent, b):
            print('YES')
        else:
            print("NO")