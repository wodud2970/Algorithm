n = input()
result = 0
string = []
for i in n:
    try :
        int(i)
        result += int(i)
    except:
        string.append(i)

print("".join(sorted(string)) + str(result))