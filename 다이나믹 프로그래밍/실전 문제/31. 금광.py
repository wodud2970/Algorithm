t = 2
for i in range(2):
    n, m = map(int, input().split())
    lst = list(map(int, input().split()))
    maps =[]
    for j in range(n):
        maps.append(lst[j * m:j * m + m])
    #오른쪽위 오른쪽 오른쪽 아래 3가지로 이동