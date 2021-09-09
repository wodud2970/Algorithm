
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
v, e = map(int, input().split())
parent = [0] * (v+1)

for  i in range(1, v+1):
    parent[i] = i

for i in range(e):
    c, a, b = map(int, input().split())
    if c == 0: #0일때 합치기
        union_parent(parent, a,b)

# 1인것을 찾아 한다
print('각 원소가 속한 집합:', end = ' ')
for i in range(1, v+1):
    print(find_parent(parent,i), end=' ')

