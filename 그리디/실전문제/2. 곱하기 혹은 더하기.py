
word = input()
result = [0] * (len(word) -1)
result[0] = max(int(word[0]) + int(word[1]), int(word[0]) * int(word[1]))

for i in range(2, len(word)):
    result[i-1] = max(result[i-2] + int(word[i]), result[i-2] * int(word[i]))

print(result[-1])