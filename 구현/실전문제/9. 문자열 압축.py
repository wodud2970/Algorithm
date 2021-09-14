#완전탐색을 수행할수 있다

def solutions(s):
    answer = len(s)
    # 1개 단위(step)부터 압축 단위를 늘려가며 확인
    for step in range(1, len(s) // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1
        #단위 (step) 크기만큼 증가시키며 이전 문자열과 비교
        for j in range(step, len(s), step):
            #이전 상태와 동일하다면 , 압축 횟수(count) 증가
            if prev == s[j:j + step]:
                count += 1
            #다른 문자열이 나왔다면 (더 이상 압축하지 못하는 경우라면)
            else:
                compressed += str(count) + prev if 

