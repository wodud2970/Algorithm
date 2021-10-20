words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???','pro?']

#queries의 인덱스와 단어들을 넣는다
idx_lst = []
for i in queries:
    lst = []
    for j in range(len(i)):
        lst.append(i[j])

    idx_lst.append(lst)
print(idx_lst)


