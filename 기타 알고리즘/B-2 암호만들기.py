n, m  = map(int, input().split())
array =  input().split()
array.sort() #사전식으로 출력해야 하므로 입력이후에 정렬 수행
#조합 사용하면됨
from itertools import combinations
#모음 2개가 꼭 있어야 한다
vowels = ('a', 'e', 'i', 'o', 'u')

# #난 이렇게 품
# comb = combinations(array, 4)
# for i in comb:
#     for j in i:
#         print(j, end = '')
#     print()



for password in combinations(array, n):
    #패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    v_count = 0
    s_count = 0
    for i in password:
        if i in vowels:
            v_count += 1
        else:
            s_count += 1
    #최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if v_count >= 1 and s_count >= 2:
        print(''.join(password))

print('--------------')

#길이가 1인 모든 암호 조합을 확인
for password in combinations(array, n):
    #패스워드에 포함된 각 문자를 확인하며 모음의 개수를 세기
    count = 0
    for i in password:
        if i in vowels:
            count += 1
    #최소 1개의 모음과 최소 2개의 자음이 있는 경우 출력
    if count >= 1 and count <= n-2:
        print(''.join(password))