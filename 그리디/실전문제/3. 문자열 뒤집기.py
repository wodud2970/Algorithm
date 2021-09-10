number = input()

#1로 뒤집을 때 0으로 뒤집을때 2가지경우
# 순서가 겹쳐져 있지 않는 경우를 센다
num_0 = 0
num_1 = 0
for i in range(1, len(number)):
    if number[i-1] != number[i]:
        if number[i] == "0":
            num_0 += 1
        else:
            num_1 += 1
print(num_0, num_1)
print(min(num_0, num_1))