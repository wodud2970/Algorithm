#재귀적으로 구현 해결가능하다  dfs (아직 재귀와 스택이 낯설다)
#어렵다 휴
#균형잡힌 괄호 문자열 인덱스 반환
def balanced_index(p):
    count = 0  #왼쪽 괄호의 개수
    for i in range(len(p)):
        if p[i] == '(':
            count += 1
        else:
            count -= 1
        #count 가 0이 되면 괄호가 알맞게 닫혀지는거
        if count == 0:
            #균형이 잡혀져잇는 index위치 반환
            return i


#올바른 괄호 문자열 인지 판단
def check_proper(p):
    count = 0
    for i in p:
        if i == '(':
            count += 1
        else:
            #빼지도 않았는데 그전에 0이되면 옳바르지 못한 괄호로 생각
            if count == 0: #쌍이 맞지 않는 경우 False 반환
                return False
            count -= 1
    return True

def solution(p):
    answer = ''
    #p가 공백일때 null 값이므로 그대로 반환
    if p == '':
        return answer
    index = balanced_index(p)
    u = p[:index + 1]
    v = p[index + 1 :]
    #'올바른 괄호 문자열'이면, v에 대해 함수를 수행한 결과를 붙여 반환
    if check_proper(u):
        # True일 경우 추가하여 다음 단계 실행
        answer = u + solution(v)
    #올바른 괄호 문자열이 아니라면 아래의 과정을 수행
        # False일 경우 '(' ')'로 끝에 추가하고 진행
    else:
        answer = '('
        answer += solution(v)
        answer += ')'
        #여기서 잘모르겟네 .... u가 올바른 괄호 문자열이 아니므로 새로운 문자열을 만든다 )(
        #첫번째와 마지막을 제거하여 옳바른 문자를 만들어준다  U의값이 맞지 않는것은 부호가 반대로 되어있기때문이다 그러므로 찾아주어서 바꾸어 준다

        u = list(u[1:-1]) #첫 번째와 마지막 문자를 제거
        for i in range(len(u)):
            if u[i] == '(':
                u[i] = ')'
            else:
                u[i] = '('
        answer += "".join(u)
    return answer
