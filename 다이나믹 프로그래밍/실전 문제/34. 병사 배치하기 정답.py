n = int(input())
array = list(map(int, input().split()))
#순서를 뒤집어 '가장 긴 증가하는 부분 수열' 문제로 변환
array.reverse()
print(array)
#다이나믹 프로그래밍을 위한 1차원 DP테이블 초기화
dp = [1] * n

#가장 긴 증가하는 부분 수열 (LIS) 알고리즘 수행
for i in range(1, n):
    # i = 4
    for j in range(0,i):
        # j = 0 1 2 3
        if array[j] < array[i]: # 4 2  5 8 < 4  True인거 한개 따라서 2
            #dp[2] = max(dp[2], dp[0] or dp[1] +1) dp[2] =2 #먼말인지 알겠지만 어렵네 ㅋㅋ 최대 가능한 갯수를 구하고 총 경우의 수를 빼는거 
            dp[i] = max(dp[i], dp[j] + 1)
            print(dp[i])
print(dp)
#열외시켜야 하는 병사의 최소 수를 출력
print(n - max(dp))