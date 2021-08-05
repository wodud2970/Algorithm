#문자열 연산을 이용

#완전탐색 24 x 60 x 60 비효율적이다  100만개 이하 일때는 이게 더좋다

# H를 입력받기
h = int(input())

count = 0

# for i in range(h+1):
#     for j in range(60):
#         for k in range(60):
#             #매 시간 안에 '3'이 포함 되어 있다면 카운트 증가
#             if '3' in str(i) + str(j) + str(k):
#                 count += 1

# print(count)

#그리드 알고리즘 유형과 큰차이가 없다

for i in range((h+1)*60*60):
    if '3' in i:
        count +=1
print(count)