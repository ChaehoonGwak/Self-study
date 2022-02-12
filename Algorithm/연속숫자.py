문제 설명
두개의 정수 a와 b에 대하여 a와 b 사이에 있는 모든 정수가 한번씩만 등장했을 때, 이를 정수가 연속한다고 말한다.

당신의 아들이 연속된 양의 정수를 임의의 순서대로 종이에 쓰고 있었다. 
이 때, 각 숫자는 정확히 한번만 쓰여졌다. 
그리고나서 그 중 하나의 숫자를 지웠다. 
아들은 어느 숫자를 지웠는지 맞춰보라고 한다.

예를 들어, (10, 7, 12, 8, 11)이 종이에 남아 있었다면 지운 숫자는 9가 된다. 
만약 남은 숫자가 (2, 3)이라면 지운 숫자는 1 혹은 4가 된다. 
남은 숫자가 (3, 6)이라면 당신의 아들이 실수한 것이다.

종이에 남은 숫자는 numbers로 주어진다. 
당신의 아들이 지웠을 가능성이 있는 모든 숫자를 정수 배열의 형태로 반환하여라. 
숫자들은 높은 차순으로 정렬되어야하며 중복되는 숫자는 없어야 한다. 
만약 아들이 실수를 했다면 아무것도 들어있지 않은 정수 배열을 반환하여라.

참고 / 제약 사항
numbers는 1개 이상, 50개 이하의 요소를 가진다.
numbers의 각 요소는 1 이상, 1000000000 이하이다.



class Solution:
    def solution(self, numbers):
        answer = []
        numbers.sort()
        compare = numbers[0]

        for number in numbers[1:]:
            if number != compare+1 and number != compare+2:
                return []
            if number != compare+1:
                answer.append(compare+1)
            compare = number
        
        if answer:
            if len(answer) > 1:
                return []
            else:
                return answer
                
        if not answer:
            if numbers[0]-1 > 0:
                answer.append(numbers[0]-1)
            answer.append(numbers[-1]+1)

        return answer
