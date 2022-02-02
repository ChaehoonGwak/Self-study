최댓값과 최솟값
문제 설명
문자열 s에는 공백으로 구분된 숫자들이 저장되어 있습니다. 
str에 나타나는 숫자 중 최소값과 최대값을 찾아 이를 "(최소값) (최대값)"형태의 문자열을 반환하는 함수, solution을 완성하세요.
예를들어 s가 "1 2 3 4"라면 "1 4"를 리턴하고, "-1 -2 -3 -4"라면 "-4 -1"을 리턴하면 됩니다.

제한 조건
s에는 둘 이상의 정수가 공백으로 구분되어 있습니다.



def solution(s):
    answer = ''
    
    numbers = s.split(' ')  # 문자열에 있는 숫자들을 공백 기준으로 split
    numbers = list(map(int, numbers))   # split한 숫자들을 int형으로 변환
    
    # 최댓값과 최솟값을 구함
    max_number = max(numbers)
    min_number = min(numbers)
    
    answer += str(min_number) + ' ' + str(max_number)   # "(최소값) (최대값)"형태의 문자열로 변환
        
    return answer
