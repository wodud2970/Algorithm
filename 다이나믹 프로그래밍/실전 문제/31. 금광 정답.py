#테스트 케이스 (test case)
for tc in range(int(input())):
    #금광정보 입력
    n, m = map(int, input().split())
    array = list(map(int, input().split()))

    #다이나믹 프로그래밍을 위한 2차원 DP 테이블 초기화
    dp = []
    index = 0
    for i in range(n):
        dp.append(array[index: index + m])
        index += m #이게 쫌 더 깔끔하네 ... array[i * m : i * m  + m ] 이렇게 했는데 ㅋㅋㅋ 똑같긴해..
        
    #다이나믹 프로그래밍 진행
    for j in range(1, m): #열부터 진행
        for i in range(n): #그 다음 어떤행인지 보기

            #왼쪽 위에서 오는 경우
            if i == 0: #첫 행
                left_up = 0
            else:
                left_up = dp[i-1][j-1]

            #왼쪽 아래에서 오는경우
            if i==n-1: #마지막 행
                left_down =0
            else:
                left_down = dp[i+1][j-1]

            #왼쪽에서 오는 경우
            left = dp[i][j-1]
            #dp테이블을 변환해서 준다
            dp[i][j] = dp[i][j] + max(left_up, left_down, left)
    result = 0
    #마지막 열을 다 비교해서 최대값을 찾는다
    for i in range(n):
        result = max(result, dp[i][m-1])

    print(result)