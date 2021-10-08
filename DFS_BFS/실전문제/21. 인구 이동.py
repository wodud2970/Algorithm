from collections import deque

#땅의 크기(N), L, R값을 입력받기
n, l, r = map(int, input().split())

#전체 나라의 정보 (NxN)를 입력받기
graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))


#상 좌 하 우
dx = [-1, 0, 1, 0]
dy = [0, -1, 0 ,1]

result = 0

#특정위치에서 출발하여 모든 연합을 체크한 뒤에 데이터 갱신
def process(x, y, index):
    #(x, y)의 위치와 연결된 나라 (연합) 정보를 담는 리스트
    united = []
    united.append((x,y)) #첫번째 국가를 통한 연합국가
    # 너비 우선 탐색(BFS)를 위한 큐 자료구조 정의
    q = deque()
    q.append((x,y))
    union[x][y] = index #현재 연합의 번호 할당
    summary = graph[x][y] #현재 연합의 전체 인구 수 #현재의 국가 인구수
    count = 1 #현재 연합의 국가 수 $연합된 국가수
    #큐가 빌 때까지 반복(BFS)
    while q:
        x,y = q.popleft()
        #현재 위치에서 4가지 방향을 확인하여 #주위 국가를 확인
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            #바로 옆에 있는 나라를 확인하여
            if 0 <= nx < n and 0 <= ny < n and union[nx][ny] == -1: #소속이 되있지 않는 국가 이면 조건 확인
                #옆에 있는 나라와 인구차이가 L명 이상 R명 이하라면
                if l <= abs(graph[nx][ny] - graph[x][y]) <= r: #인구가 들어올수 있는지 확인
                    q.append((nx, ny)) #들어올수 있다면 q에 입력 입력되어 다음 국가를 찾아본다
                    #연합에 추가
                    union[nx][ny] = index #연합에 추가 #union이 바뀌지 않으면 인구이동이 나타나지 않은거다
                    #연합국가 인구수를 더하기
                    summary += graph[nx][ny] #연합된 국가 인구수 더하기
                    #몇개가 더해 졌는지 확인 #국가 몇개가 더해졌는지 확인
                    count +=1
                    united.append((nx, ny)) #연합 죄표를 추가
    #연합 국가끼리 인구를 분배 (연합 국가 끼리)
    for i, j in united: #총 연합좌표를 국가가 동일한 인구를 가지게 만들어줌
        graph[i][j] = summary //count
    return count

total_count = 0

#더 이상 인구 이동을 할 수 없을 때까지 반복
while True:
    union = [[-1] * n for _ in range(n)] #연합국가 갯수 세는거
    index = 0
    for i in range(n):
        for j in range(n):
            if union[i][j] == -1: #해당나라가 아직 처리 되지 않았다면
                process(i, j, index)
                index += 1 #다른 연합국가를 생성하기 위해 index를 늘려줌

    #모든 인구 이동이 끝난 경우 #너비 탐색으로 총 몇번 일어나는지 확인
    if index == n * n :
        break
    total_count += 1

#인구 이동 회수 출력
print(total_count)