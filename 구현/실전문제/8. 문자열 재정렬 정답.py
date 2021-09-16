data = input()
result = []
value = 0

#문자를 하나씩 확인하며
for x in data:
    #알파벳인 경우 결과 리스트에 삽입
    if x.isalpha():
        result.append(x)
    else:
        value += int(x)

#알파벳을 오름차순으로 정렬
result.sort()
if value != 0:
    result.append(str(value))
print(''.join(result))