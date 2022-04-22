문제 설명
한자리 숫자가 적힌 종이 조각이 흩어져있습니다. 흩어진 종이 조각을 붙여 소수를 몇 개 만들 수 있는지 알아내려 합니다.

각 종이 조각에 적힌 숫자가 적힌 문자열 numbers가 주어졌을 때, 종이 조각으로 만들 수 있는 소수가 몇 개인지 return 하도록 solution 함수를 완성해주세요.

제한사항
numbers는 길이 1 이상 7 이하인 문자열입니다.
numbers는 0~9까지 숫자만으로 이루어져 있습니다.
"013"은 0, 1, 3 숫자가 적힌 종이 조각이 흩어져있다는 의미입니다.



from itertools import permutations

def solution(numbers):
    answer = []
    comb = set()
    
    for i in range(len(numbers)): # 종이 조각으로 만들 수 있는 모든 수 조합
        comb |= set(map(int, map(''.join, permutations(list(numbers), i+1))))
    
    # 0과 1은 판별 X
    if 0 in comb: comb.remove(0) 
    if 1 in comb: comb.remove(1)
    
    for i in range(2, int(max(comb)**0.5)): # 소수 판별 후 모든 수 조합에서 소수가 아닌 수 제거
        comb -= set(range(i*i, max(comb)+1, i))

    answer = len(comb) # 남아있는 원소 수가 종이 조각으로 만들 수 있는 모든 소수의 갯수
    
    return answer
