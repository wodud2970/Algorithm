#삼각형 행
n = int(input())
#삼각형을 만드는 리스트
triangle= []
for i in range(n):
        triangle.append(list(map(int, input().split())))

print(triangle)
#7
#3 8
#8 1 8
# dp 테이블 만들기
dp = triangle.copy()
for i in range(1,n):
        for j in range(i+1):
                #첫번째 줄
                if j == 0 :
                        triangle[i][j] = triangle[i][j] + triangle[i-1][j]
                        print(triangle[i][j])
                #마지막 줄
                elif j == len(triangle[i]) - 1:
                        triangle[i][j] = triangle[i][j] + triangle[i-1][j-1]
                #나머지 중간값
                else:
                        triangle[i][j] = max(triangle[i-1][j-1] , triangle[i-1][j]) + triangle[i][j]

print(triangle)
print(max(triangle[n-1]))