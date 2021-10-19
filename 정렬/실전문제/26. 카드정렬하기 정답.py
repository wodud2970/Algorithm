#heapq를 이용함
import heapq

n = int(input())

#힙(heap)에 초기 카드 묶음을 모두 삽입
heap = [] #빈 리스트에다 heap을 해놓는구나
for i in range(n):
    data = int(input())
    heapq.heappush(heap, data)
print(heap) #순서에 맞게 정렬해준다 우선순위큐 인거 같다 따로 sort를 안해줘도 되는듯

result = 0
#힙(Heap)에 원소가 1개 남을때까지
while len(heap) != 1:
    #가장 작은 2개의 카드 묶음 커내기
    one = heapq.heappop(heap)
    two = heapq.heappop(heap)

    #카드 묶음을 합쳐서 다시 삽입
    sum_value = one + two
    result += sum_value
    heapq.heappush(heap, sum_value)

print(result)