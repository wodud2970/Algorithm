#점화식 max(a_(i-1), a_(i-2) + k)

#정수 N을 먼저 받기
n = int(input())
#모든 식량 정보 입력받기
array = list(map(int, input().split()))

#앞서 계산된 결과를 저장하기위한DP테이블 초기화
d = [0] * 100

#다이나믹 프로그래밍 진행(보텀업)

d[0] = array[0] #첫번째
d[1] = max(array[0], array[1]) # 두번째

for i in range(2,n):
    #중간값 한개, 왼쪽값, 오른쪽값
    d[i] = max(d[i-1], d[i-2] + array[i])

print(d)
print(d[n-1])