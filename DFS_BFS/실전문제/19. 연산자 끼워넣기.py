from itertools import combinations #조합
from itertools import permutations #순열


num = int(input())
permu = list(map(int, input().split()))
calculate_lst = list(map(int, input().split()))

# max_num = 0
# min_num = 9999999999999
# permu = list(permutations(permu, num))
# print(permu)
# for permutation in permu:
#     #순열이 바뀔때마다
#     per_num = 1
#     #시작은 첫번째 걸로
#     result = permutation[0]
#     for i in range(len(calculate_lst)):
#         #모든 순열을 계산 해본다
#         copy_lst = calculate_lst.copy()
#         while copy_lst[i] != 0: #calculate_lst 가 최기화가 안되서 그렇네 ...
#             if i == 0:
#                 result = result + permutation[per_num]
#             elif i == 1:
#                 result = result - permutation[per_num]
#             elif i == 2:
#                 result = result * permutation[per_num]
#             elif i == 3:
#                 result = result // permutation[per_num]
#             copy_lst[i] -= 1
#             per_num += 1
#             #끝나면 최대 최소 비교하고
#             print(result)
#
#     max_num = max(result, max_num)
#     min_num = min(result, min_num)
# print(max_num, min_num)

# 부호 순서만 조합으로 해서 만들어보기 위에꺼는 숫자 순서를 순열로 해놓은것
result = permu[0]


#부호값 리스트에 넣어주기
cal_kind = []
for i in range(len(calculate_lst)):
    while calculate_lst[i] != 0:
        if i == 0 :
            cal_kind.append('+')
        elif i == 1:
            cal_kind.append('-')
        elif i == 2:
            cal_kind.append('*')
        else:
            cal_kind.append('/')
        calculate_lst[i] -= 1

print(cal_kind)

cal_lst = list(permutations(cal_kind, num-1))
#숫자값을 넣어주어서 계산
max_num = -1e9
min_num = 1e9
# for i in range(1, len(permu)):
#     result = permu[0]
#     for j in cal_lst:
#         if j[i-1] == '+':
#             result += permu[i]
#         elif j[i-1] == '-':
#             result -= permu[i]
#         elif j[i-1] == '*':
#             result *= permu[i]
#         else:
#             result //= permu[i]
#         print(result)
#     max_num = max(result, max_num)
#     min_num = min(result, min_num)
print(cal_lst)
#예시 3번이 왜 안풀리는지 모르곘다 ㅠ
for i in cal_lst:
    result = permu[0]
    for j in range(len(i)):
        if i[j] == '+':
            result += permu[j+1]
        elif i[j] == '-':
            result -= permu[j+1]
        elif i[j] == '*':
            result *= permu[j+1]
        else:
            result //= permu[j+1]
        print(result)
    max_num = max(result, max_num)
    min_num = min(result, min_num)
print(max_num)
print(min_num)









