가장 큰 수
문제 설명
0 또는 양의 정수가 주어졌을 때, 정수를 이어 붙여 만들 수 있는 가장 큰 수를 알아내 주세요.

예를 들어, 주어진 정수가 [6, 10, 2]라면 [6102, 6210, 1062, 1026, 2610, 2106]를 만들 수 있고, 이중 가장 큰 수는 6210입니다.

0 또는 양의 정수가 담긴 배열 numbers가 매개변수로 주어질 때, 순서를 재배치하여 만들 수 있는 가장 큰 수를 문자열로 바꾸어 return 하도록 solution 함수를 작성해주세요.

제한 사항
numbers의 길이는 1 이상 100,000 이하입니다.
numbers의 원소는 0 이상 1,000 이하입니다.
정답이 너무 클 수 있으니 문자열로 바꾸어 return 합니다.



def solution(numbers):
    numbers = map(str, numbers) # numbers 문자열로 변환
    numbers_dict = [] # 같은 수가 존재할 수 있으므로 중복이 불가능한 dict는 사용하지 않음
    
    for number in numbers:
        number_len = len(number)
        temp = number
        
        if number_len==1: # 1자리수라면 해당 수로 4자리수를 만듦
            temp += number * 3
        elif number_len == 2: # 2자리수라면 해당 수로 4자리수를 만듦
            temp += number
        elif number_len == 3: # 3자리수라면 해당 수 맨 앞 수로 4자리수를 만듦
            temp += number[0]
            
        numbers_dict.append([number, temp]) # 해당 수와 4자리수를 리스트로 삽입
    
    numbers_dict = sorted(numbers_dict, key=lambda x:x[1], reverse=True) # 4자리수 기준으로 정렬
    
    if numbers_dict[0][0] == "0": # "0" case 존재하므로 조건문을 통해 해당 케이스 처리
        answer = "0"
    else:
        answer = ''.join(map(lambda x:x[0], numbers_dict)) # 가장 큰 수를 하나의 문자열로 만듦
    
    return answer
