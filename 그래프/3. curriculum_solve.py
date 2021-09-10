from collections import deque
import copy
#<--------------------어려웡------------------->
#노드의 개수 입력받기
v =  int(input())

#모든 노드에 대한 진입차수는 0으로 초기화
indegree = [0] *  (v+1)

#각 노드에 연결된 간선정보를 담기 위한 연결 리스트 (그래프) 초기화
graph = [[] for i in range(v+1)]

#각 강의 시간을 0으로 초기화 #가중치를 넣어주기위해 만든다
time = [0] * (v+1)

#방향 그래프의 모든 간선정보를 입력받기
for i in range(1, v+1):
    data = list(map(int, input().split()))
    time[i] = data[0] #첫 번째 수는 시간 정보를 담고 있음
    for x in data[1:-1]:
        indegree[i] += 1 #연결당하는 간선저장 진입차수
        graph[x].append(i) #연결하는 간선 저장

#위상 정렬함수
def topology_sort():
    result = copy.deepcopy(time) #알고리즘 수행결과를 담을 리스트 #왜 리스트를 이렇게 담냐 -> 단순히 대입 연산을 하면 값이 변경될때 문제가 발생할 수 있기 때문에
    q = deque()


    #처음 시작할 때는 진입차수가 0인 노드를 큐에 삽입
    for i in range(1, v+1):
        if indegree[i] == 0:
            q.append(i)
    while q:
        #큐에서 원소 꺼내기
        now = q.popleft()
        #해당 원소와 연결된 노드들의 진입차수에서 1뺴기
        for i in graph[now]: #연결되있는 거 찾기
            result[i] = max(result[i], result[now] + time[i]) #순서를 넣는게아니라 값을 넣기
            indegree[i] -= 1 #간선 빼기 #진입차수를 0으로 만든다
            #새롭게 진입차수가 0이 되는 노드를 큐에 삽입
            if indegree[i] ==0:
                q.append(i)

    #위상 정렬을 수행한 결과 출력
    for i in range(1, v+1):
        print(result[i])

topology_sort()