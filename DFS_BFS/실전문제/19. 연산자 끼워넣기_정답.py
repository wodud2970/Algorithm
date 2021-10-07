#DFS 혹은 BFS를 이용하여 문제를 해결할 수 있다
# 중복순열을 이용하여 푸는 방법
from itertools import product #순열을 이용하여 풀어도된다
n = 4
print(product(['+', '-', '*', '/'], repeat = (n-1))) #내가 푼 방법
print(list(product(['+', '-', '*', '/'], repeat = (n-1))))

n = int(input())

#연산을 수행하고자 하는 수 리스트
data = list(map(int, input().split()))

# 더하기, 빼기, 곱하기 나누기 연산자 개수
add, sub, mul, div = map(int, input().split())

# 최솟값과 최댓값 초기화
min_value = 1e9
max_value = -1e9

#깊이 우선 탐색 (DFS) 메서드
def dfs(i, now):
    global min_value, max_value, add, sub, mul, div
    #모든 연산자를 다 사용한 경우, 최솟값과 최댓값 업데이트
    if i == n:
        min_value = min(min_value, now)
        max_value = max(max_value, now)
    else:
        #각 연사자에 대하여 재귀적으로 수행
        if add > 0:
            add -= 1 #하나씩 차감
            # i가 계속증가, 그에따라 now data도 변화 -> 변화가 끝난후 다음차례
            dfs(i+1, now+data[i])
            #dfs(2, now +)
            #dfs(3, now ++)
            add += 1 #마지막에 더해줌으로써 리셋을 하고 랜덤으로 탐색을 해주기위해서 (다른 여러방법을 이용하기위해서)
        if sub > 0 :
            sub -= 1
            dfs(i+1, now-data[i])
            sub += 1
        if mul > 0 :
            mul -= 1
            dfs(i+1, now*data[i])
            mul += 1
        if div > 0:
            div -= 1
            dfs(i+1, now//data[i])
            div += 1

#DFS 메서드 호출
dfs(1, data[0])
print(max_value)
print(min_value)