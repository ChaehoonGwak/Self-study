Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

An input string is valid if:

Open brackets must be closed by the same type of brackets.
Open brackets must be closed in the correct order.



class Solution:
    def isValid(self, s: str) -> bool:
        stack = [] # 스택
        parentheses = {')':'(', '}':'{', ']':'['} # 일치하는 괄호들을 딕셔너리로 정리
        keys = list(parentheses.keys()) # 닫는 괄호들
        values = list(parentheses.values()) # 여는 괄호들
        
        for c in s:
            if stack and c in keys and stack[-1] == parentheses[c]: # 스택의 탑이 c의 여는 괄호라면 pop
                stack.pop()
            elif c in keys: # 스택의 탑이 c의 여는 괄호가 아니면서, c가 닫는 괄호라면 False 리턴
                return False
            elif c in values: # 여는 괄호는 push
                stack.append(c)
                
        if stack: # s를 다돌고 스택에 값이 남아있다면 False 리턴, 빈 스택이라면 True 리턴
            return False
        else:
            return True
        
