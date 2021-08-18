# MxN 크기의 얼음틀이있다 구멍이 뚫려 있는 부분은 0 존재하는 부분은 1
#구멍이 뚫려있는 부분끼리 상하좌우로 붙어있으면 서로 연결로 간주

#노드 끼리 탐색하고 다 탐색하면 다음 노드로 이동
N , M = map(int,input().split())

# 맵
graph = [[int(i) for i in list(input())] for _ in range(N) ]

# graph = []
# for i in range(N):
#     graph.append(list(map(int,input())))
# print(graph)

#노드정보 입력
def dfs(x,y):
    # 주어진 범위를 벗어나는 경우 즉시 종류
    if x<= -1 or x>= N or y<=-1 or y >=M:
        return False
    #현재 노드에 방문하지 않았다면
    if graph[x][y] ==0:
        #해당 노드 방문철
        graph[x][y]=1
        #상, 하, 좌, 우의 위치도 모두 재귀적으로 호출
        dfs(x-1,y)#상
        dfs(x,y-1)#좌
        dfs(x+1, y)#하
        dfs(x,y+1)#우
        return True
#모든 노드(위치)에 대하여 음료수 채우기
result = 0
for i in range(N):
    for j in range(M):
        #현재 위치에서 DFS 수행
        if dfs(i,j) == True:
            result +=1

print(result)