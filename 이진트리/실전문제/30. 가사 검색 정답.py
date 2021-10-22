from bisect import bisect_left, bisect_right

#값이 [left_value, right_value]의 데이터와 개수를 반환하는 함수
def count_by_range(a, left_value, right_value):
    right_index = bisect_right(a, right_value)
    left_index = bisect_left(a, left_value)
    print(left_index, right_index, a, left_value, right_value)
    return right_index - left_index

#모든 단어를 길이마다 나누어서 저장하기위한 리스트
array = [[] for _ in range(10001)]
#모든 단어를 길이마다 나누어서 뒤집어 정하기 위한 리스트
reversed_array = [[] for _ in range(10001)]

words = ['frodo', 'front', 'frost', 'frozen', 'frame', 'kakao']
queries = ['fro??', '????o', 'fr???', 'fro???','pro?']

def solution(words, queries):
    answer = []
    #일단 단어 개수가 맞는지 확인
    for word in words: #모든 단어를 접미사 와일드카드 배열, 접두사 와일드카드 배열에 각각 삽입 #갯수를 보고 삽입
        array[len(word)].append(word) #단어를 삽입
        reversed_array[len(word)].append(word[::-1]) #단어를 뒤집어서 삽입

    for i in range(10001): #이진 탐색을 수행하기 위해 각 단어 리스트 정렬 수행 #단어 전체를 sorting
        array[i].sort()
        reversed_array[i].sort()

    for q in queries: #쿼리를 하나씩 확인하며 처리
        if q[0] != '?': #접두사가 ?이 아닐때 뒤에서 부터 확인 왜냐하면 접미사랑 접두사만 가능하다고 해서 뒤에것이 ?
            #q의 갯수로 5개인것만 ? 가 왼쪽은 a로 변환 ? 가 오른쪽은 z로 변환 하여 값을 빼준다  array[5] frodo, froaa크거나 같으면서 frozz보다 작거나 같은 단어의 개수를 센다 문자열을 단어로 취급해주는것
            res = count_by_range(array[len(q)], q.replace('?','a'), q.replace('?','z'))
        else: #접두사 reversed 거꾸로된 words q값도 뒤집어 주어서 o????순으로 바꾸어준다 그래서 그거의 단어를 세주어 개산하여 찾아줌 미친 시발 이걸 어떻게 생각 해 시발발
            res = count_by_range(reversed_array[len(q)], q[::-1].replace('?', 'a'), q[::-1].replace('?','z'))
        #검색된 단어의 개수를 저장
        answer.append(res)
    return answer
print(solution(words, queries))