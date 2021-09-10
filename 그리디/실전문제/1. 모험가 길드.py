#모험가수
n = int(input())

member = list(map(int, input().split()))

result = 0
#공포도 기사 종류
for i in set(member):
    count = 0
    #종류의 개수를 세줌
    for j in member:
        if  j== i:
            count += 1
    #기사의 공포도 종류를 세서 나누어줌
    result += (count // i)
print(result)