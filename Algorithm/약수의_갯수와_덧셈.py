약수의 개수와 덧셈
문제 설명
두 정수 left와 right가 매개변수로 주어집니다. 
left부터 right까지의 모든 수들 중에서, 약수의 개수가 짝수인 수는 더하고, 
약수의 개수가 홀수인 수는 뺀 수를 return 하도록 solution 함수를 완성해주세요.

제한사항
1 ≤ left ≤ right ≤ 1,000



def solution(left, right):
    answer = 0
    numbers = [x for x in range(left, right+1)]
    
    for number in numbers:
        divisor = []
        for i in range(1, number+1):
            if (number % i) == 0:
                divisor.append(i)
        if len(divisor) % 2 == 0:
            answer += number
        else: answer -= number
        
    return answer
