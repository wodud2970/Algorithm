#N은 행의 개수 M은 열의개수
#1. 행을 먼저 선택
#2. 행에 포함된 카등중 가장 낮은 카드를 뽑아야한다
#3. 처음에 카드를 골라낼 행을 선택할 때, 이후에 해당 행에서 가장 숫자가 낮은 카드를 뽑을것을 고려하여 최정적으로 가장 높은 숫자의 카드를 뽑을수 있도록 해야한다

#행렬을 만든다 N x M
n, m = map(int, input().split())

# data  = [[0] * m for i in range(n)]

answer = 0
for i in range(n):
    data = map(int,input().split())
    mini = min(data)
    if answer < mini:
        answer = mini

print(answer)

