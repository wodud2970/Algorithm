n = int(input()) #전체 상담개수
t = [] #각 상담을 완료하는데 걸리는 시간
p = [] #각 상담을 완료했을 때 받을 수 있는 금액
dp = [0] * (n+1) #다이나믹 프로그래밍을 위한 1차원 dp 테이블 초기화


for _ in range(n):
    x, y = map(int, input().split())
    #걸리는 시간
    t.append(x)
    #상담 완료후 받을 수 있는 금액
    p.append(y)

max_value = 0
#리스트를 뒤에서부터 거꾸로 확인
for i in range(n-1, -1, -1):
    time = t[i] + i
    #상담이 기간 안에 끝나는 경우 #뒤에서 부터 되는경우를 계산
    if time <= n :
        #점화식에 맞게 현재까지의 최고 이익 계산
        dp[i] = max(p[i] + dp[time], max_value)
        max_value =dp[i]
    #상담이 기간을 벗어나는 경우
    else: #상담기간이 이 퇴사 기간보다 긴경우 (어차피  안되는경우)
        dp[i] = max_value

print(dp)
print(max_value)