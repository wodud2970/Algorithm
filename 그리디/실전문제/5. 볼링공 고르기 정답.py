#n이 공의 갯수 m이 최대 무개
n, m = map(int, input().split())
data = list(map(int, input().split()))

# 1부터 10까지의 무게륻 담을 수 있는 리스트
array = [0] * 11

for x in data:
    # 각 무게에 해당하는 볼링공의 개수 카운트
    array[x] += 1


# 진짜 그리드 알고리즘은 수학 공부다 진짜로 ㅠ
# 전체의 경우의 수 * 남아있는 무게의 공 갯수를 곱한다
result = 0
# 1부터 m까지의 각 무게에 대하여 처리
for i in range(1, m + 1):
    n -= array[i] #무게가 볼링공의 개수 (A가 선택할 수 있는 개수) 제외
    result += array[i] * n #B가 선택하는 경우의 수와 곱하기
print(result)