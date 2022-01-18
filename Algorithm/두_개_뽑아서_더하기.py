두 개 뽑아서 더하기
문제 설명
정수 배열 numbers가 주어집니다. 
numbers에서 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수를 배열에 오름차순으로 담아 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers의 길이는 2 이상 100 이하입니다.
numbers의 모든 수는 0 이상 100 이하입니다.



from itertools import combinations

def solution(numbers):
    answer = []
    
    # 서로 다른 인덱스에 있는 두 개의 수를 뽑아 더해서 만들 수 있는 모든 수의 조합
    comb = list(map(sum, combinations(numbers, 2)))
    
    for n in comb: # 중복인 수 제거
        if n not in answer:
            answer.append(n)
            
    answer.sort() # 오름차순으로 정렬
    
    return answer
