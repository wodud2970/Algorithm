
# a_i-k를 만드는 방법이 존재하는 경우 a = min(a_i, a_i-k + 1)
# a_i-k를 만드는 방법이 존재하지 않는 경우 a_i = 10001 (m의 값은 10000 이하 이기 때문에 10001을 넣는다 )
# 10001이라는 값은 특정금액을 만들수 있는 화폐구성이 가능하지않다는 의미

# 정수 N, M 을 입력받기
n, m = map(int, input().split())

# N 개의 화폐 단위 정보를 입력받기
array = [int(input()) for _ in range(n)]

#한 번 계산된 결과를 저장하기 위한 Dp 테이블 초기화
d = [10001] * (m+1)

#다이나믹 프로그래밍 진행
d[0] = 0

for i in range(n):
    #사용할수 있는 array값들
    for j in range(array[i], m+1):
        # 0 부터 시작 앞에 것들은 계산 안해줘도 되기 떄문에 ( 10001이 아닌것들을 계산해준다)
        if d[j - array[i]] != 10001: #(i-k)원을 만드는 방법이 존재하는 경우 #이것 때문에 i 값을 따로 뺏구나
            #기준의 값 과 값 - array 값 + 1 을 비교
            d[j] = min(d[j], d[j - array[i]]+ 1)
#계산된 결과 출력
if d[m] == 10001:
    print(-1)
else:
    print(d[m])
