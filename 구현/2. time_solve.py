N = int(input())
num = 0
for i in range(N+1):
    minute =0
    second =0
    while minute < 60:
        second=0
        minute += 1
        while second < 60:
            if '3' in str(minute) or '3' in str(second) or i == 3:
                num +=1
            second += 1

print(num)