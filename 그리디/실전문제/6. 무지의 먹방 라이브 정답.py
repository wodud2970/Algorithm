#heapq 와 계산식이 좀어려움 이진트리 써서 그런지

import heapq
def solution(food_times, k):
    #전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    #시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        #(음식시간, 음식번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))

        sum_value = 0 #먹기 위해 사용한 시간
        previous = 0 # 직전에 다 먹은 음식 시간
        length  = len(food_times)

        #sum value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k비교
        # 12 + ((다음 음식(6 - 4 ) * 2 ) 16이라서 꺠짐 <=
        while sum_value + ((q[0][0] - previous) * length) <= k:
            #현재의 음식 시간
            now = heapq.heappop(q)[0]
            sum_value += (now - previous) * length # sum_value =  12
            length -= 1 # length  = 2
            previous = now # previous  = 4

    #남은 음식중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key = lambda x: x[1]) #음식 번호 기준으로 정렬 2번음식
    #몇 번 째 음식인지 찾는다
    return result[(k-sum_value) % length][1]