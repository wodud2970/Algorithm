#투 포인터 알고리즘
n = 5 #데이터의 개수 n
m = 5 #찾고자하는 부분합 m
data = [1,2,3,2,5]

count = 0
interval_sum = 0
end = 0



#start를 차례대로 증가시키며 반복
for start in range(n):
    #end를 가능한 만큼 이동시키기
    #덧 셈은 찾고자하는 부분 합보다 작아야하고 그리고 끝자리느느 데이터수보다 작아야함
    while interval_sum < m and end < n:
        interval_sum += data[end]
        end += 1
    #부분합이 m일 때 카운트 증가 찾고자하는 부분합이 같을 때
    if interval_sum == m :
        count += 1
    #찾고자 하는 부분합이 더 클때 start를 옯겨준다 작으면 커질때까지 끝부분을 옮긴다
    interval_sum -= data[start]

print(count)

