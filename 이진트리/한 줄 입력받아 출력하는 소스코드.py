import sys

#하나의 문자열 데이터 입력받기
input_data = sys.stdin.readline().rstrip() #readline()으로 입력하며 입력 후 엔터가 줄 바꿈 기호로 입력이 된다 이 공백 문자를 제거하려면 rstrip() 함수를 사용해야한다

#입력 받은 문자열 그대로 출력
print(input_data)