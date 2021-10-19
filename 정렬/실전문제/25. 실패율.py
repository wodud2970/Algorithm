n = int(input())
stages = list(map(int, input().split()))
#깬 순서를 sorting 함
stages.sort()
print(stages)
#실패율을 담는 리스트
fail_lst = [0] * (n+1)
#success lst
success_lst = [0] * (n+2)

for i in range(len(stages)):
    success_lst[stages[i]] += 1
print(success_lst)


#실패율을 넣어준다
for i in range(len(success_lst)-1):
    fail = success_lst[i]/(sum(success_lst[i:]))
    fail_lst[i] = (i,fail)
fail_lst = fail_lst[1:]
fail_lst.sort(key = lambda x : ( -x[1], x[0] ))
for i in fail_lst:
    print(i[0], end = ' ')