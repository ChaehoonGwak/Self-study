JadenCase 문자열 만들기
문제 설명
JadenCase란 모든 단어의 첫 문자가 대문자이고, 그 외의 알파벳은 소문자인 문자열입니다.
문자열 s가 주어졌을 때, s를 JadenCase로 바꾼 문자열을 리턴하는 함수, solution을 완성해주세요.

제한 조건
s는 길이 1 이상 200 이하인 문자열입니다.
s는 알파벳과 숫자, 공백문자(" ")로 이루어져 있습니다.
숫자는 단어의 첫 문자로만 나옵니다.
숫자로만 이루어진 단어는 없습니다.
공백문자가 연속해서 나올 수 있습니다.
첫 문자가 영문이 아닐때에는 이어지는 영문은 소문자로 씁니다. ( 첫번째 입출력 예 참고 )



def solution(s):
    answer = []
    words = s.lower()   # 문자열 s를 모두 소문자로 변경
    words = words.split(' ')    # 공백문자를 기준으로 split
    
    for word in words:
        if len(word) == 0:  # 공백문자가 연속해서 나올 수 있으므로 공백문자 처리
            temp_word = ''
        elif word[0].islower():   # 단어의 첫 글자가 소문자라면 대문자로 변경
            temp_word = word[0].upper()
            temp_word += word[1:]
        else:
            temp_word = word    # 단어의 첫 글자가 대문자거나 숫자라면 변경 X
            
        answer.append(temp_word)    # 리스트에 삽입

    return ' '.join(answer) # 주어진 문자열과 같이 띄어쓰기를 하여 결과 리턴
