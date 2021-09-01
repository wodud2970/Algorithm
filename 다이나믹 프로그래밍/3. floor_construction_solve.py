n = int(input())

d = [0] * 100

d[0] = 1
d[1] = 3
#짝수 일때 홀수 일때를 구분하면된다
for i in range(2,n):
    d[i] =  (d[i-1] + d[i-2] * 2)

print(d[n-1])