#순열을 이용
from itertools import permutations
n = 12
weak = [1,5,6,10]
dist = [1,2,3,4]

#내 생각
# 시계방향, 반시계  /  가까이에 붙어있는 판수를 비교
# weak 1 5 6 10 => 3 4 1 4
# weak 1 3 4  9 10 => 3 2 1 5 1 / 1 5 1 2  이거 너무 어렵네
# 거리가 가까이 있는 거 끼리 계산 반시계도 있구나

#풀 이
#완전 탐색으로 해결할수 있다
#투입해야 하는 친구 수의 최솟값 -> 모든 순열의 개수를 계산  친구수가 3명 = 3!
# 길이를 2배로 늘려서 '원형'을 일자 형태로 만드는 작업

def solution(n, weak, dist):
    #길이를 2배로 늘려서 '원형'을 일자 형태로 변형 (시계 반시계 구분을 없애주기위해)
    length = len(weak)
    for i in range(length):
        weak.append(weak[i] + n)

    answer = len(dist) + 1 #투입할 친구 수의 최솟값을 찾아야 하므로 len(dist) + 1로 초기화 그냥 최기화

    # 0부터 length -1 까지의 위치를 각각 시작점으로 설정 (시작위치)
    for start in range(length):
        # 친구를 나열하는 모든 경우의 수 각각에 대하여 확인 (모든 친구 순열을 구해보단)
        for friends in list(permutations(dist, len(dist))):
            count = 1 #투입할 친구의 수
            #해당 친구가 점검할 수 있는 마지막 위치
            position = weak[start] + friends[count - 1]

            #시작점부터 모든 취약 지점을 확인
            for index in range(start, start + length):
                #점검할 수 있는 위치를 벗어나는 경우 (점검을 하지 못할 때)
                if position < weak[index]:
                    count += 1 #새로운 친구를 투입
                    if count > len(dist): #더 투입이 불가능하다면 종료 (친구의 수보다 count가 많으면)
                        break
                    #다음시작점 + 다른 친구가 점검할수있는 구역 마지막위치
                    position = weak[index] + friends[count - 1]
            answer = min(answer, count)
    #친구들로 전부 돌지 못할 때
    if answer > len(dist):
        return -1
    return answer
print(solution(n, weak, dist))