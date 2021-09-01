
n = int(input())
count = 0
# 26 25 5 1 27  9 3 1
while True:
    if n == 1:
        break
    if n % 5 == 0:
        n //= 5
    elif n % 3 == 0:
        n //= 3
    elif n % 2 == 0:
        n //= 2
    else:
        n -= 1
    print(n)
    count += 1

print(count)