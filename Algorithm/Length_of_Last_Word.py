Given a string s consisting of some words separated by some number of spaces, return the length of the last word in the string.

A word is a maximal substring consisting of non-space characters only.



class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        last_word_idx = len(words) - 1
        
        while words[last_word_idx] == '': # 공백이 포함된 경우가 있어, 공백이 아닌 마지막 단어의 인덱스를 구함
            last_word_idx -= 1
        
        return len(words[last_word_idx]) # 마지막 단어의 길이를 리턴
