큰 수 만들기
문제 설명
어떤 숫자에서 k개의 수를 제거했을 때 얻을 수 있는 가장 큰 숫자를 구하려 합니다.

예를 들어, 숫자 1924에서 수 두 개를 제거하면 [19, 12, 14, 92, 94, 24] 를 만들 수 있습니다. 이 중 가장 큰 숫자는 94 입니다.

문자열 형식으로 숫자 number와 제거할 수의 개수 k가 solution 함수의 매개변수로 주어집니다. number에서 k 개의 수를 제거했을 때 만들 수 있는 수 중 가장 큰 숫자를 문자열 형태로 return 하도록 solution 함수를 완성하세요.

제한 조건
number는 1자리 이상, 1,000,000자리 이하인 숫자입니다.
k는 1 이상 number의 자릿수 미만인 자연수입니다.



def solution(number, k):
    stack = [number[0]] # 스택에 첫 수를 넣음
    
    for num in number[1:]:
        while len(stack) > 0 and stack[-1] < num and k > 0: # 스택이 비어있지 않고 현재 숫자가 스택을 pop한 숫자보다 크며 제거할 수 있으면 계속해서 제거
            k -= 1
            stack.pop()
            
        stack.append(num) 
        
    if k != 0: # 제거할 수 있는만큼 제거하지 않은 경우 뒤에서부터 나머지를 제거함
        stack = stack[:-k]
        
    return ''.join(stack) # 결과를 문자열로 출력
