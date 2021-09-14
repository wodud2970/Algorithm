n = input()
start = n[:(len(n)//2)]
end = n[len(n)//2:]

sum_start = 0
sum_end = 0

for i in range(len(n)//2):
    sum_start += int(start[i])
    sum_end += int(end[i])

if sum_start == sum_end :
    print('Lucky')
else:
    print('READY')