#chess
#수평으로 두 칸 이동한 뒤에 수직으로 한칸 이동
#수직으로 두칸 이동한 뒤에 수평으로 한칸 이동하기
word = input()
eng = ['a','b','c','d','e','f','g','h']

x, y = int(word[1]), eng.index(word[0])+1
num = 0
dx = [-2,2]
dy = [1,-1]
for k in range(2):
    for i in dx:
        for j in dy:
            nx = x + i
            ny = y + j
            if  nx <= 8 and ny <= 8 and nx >=1 and ny >=1:
                num += 1
    dx, dy =dy, dx
print(num)
