n = int(input())

#
lst = [int(input()) for i in range(n)]
lst.sort()
print(lst)

# lst  = [10, 20, 40]
# result = [10, 20, 30, 100]
#구현 lst
result = [0] * (n)
result[0],result[1] = lst[0], lst[1]
for i in range(2,n):
    result[i] = lst[i] + sum(result[:i])

print(result, sum(result))

    #[10, 20, 30, 40 ]