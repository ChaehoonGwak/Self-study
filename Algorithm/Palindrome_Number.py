Given an integer x, return true if x is palindrome integer.

An integer is a palindrome when it reads the same backward as forward.

For example, 121 is a palindrome while 123 is not.



class Solution:
    def isPalindrome(self, x: int) -> bool:
        str_x = str(x)
        left, right = 0, len(str_x)-1 # 투 포인터
        
        while left < right: # 양쪽 끝부터 비교
            if str_x[left] != str_x[right]: # 다르면 False 리턴
                return False
            left += 1
            right -= 1
            
        return True # Palindrome 만족한다면 True 리턴
