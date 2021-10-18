n = int(input())

student = []



for i in range(n):
    student.append(list(input().split()))

student.sort(key=lambda x : str(x[0])) ##4
student.sort(key=lambda x:int(x[3]), reverse=True) ##3
student.sort(key = lambda x : int(x[2])) ## 2
student.sort(key = lambda x: int(x[1]), reverse = True)##1


for i in student :
    print(i[0])


