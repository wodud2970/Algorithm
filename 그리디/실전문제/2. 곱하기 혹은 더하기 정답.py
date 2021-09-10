#두 수에 대하여 연산을 수행할 때 , 두수 중에서 하나라도 1이하인 경우에는 더하며 두수가 모두 2 이상인 경우 곱하면된다
#나는 다이나믹으로 풀었다..

data = input()

#첫 번째 문자를 숫자로 변경하여 대입
result = int(data[0])
for i in range(1, len(data)):
    #두 수중 하나라도 0 or 1인 경우 곱하기보다 더하기수행
    num = int(data[i])
    if num <= 1 or result <= 1:
        result = num + result
    else:
        reult = num * result

print(result)