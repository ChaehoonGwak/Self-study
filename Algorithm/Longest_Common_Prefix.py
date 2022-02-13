Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        answer = ""
        min_length = min(map(len , strs)) # 가장 짧은 문자열의 길이
        
        for i in range(min_length): # 가장 짧은 문자열의 길이만큼 탐색
            compare = strs[0][i] # 첫번째 문자열을 기준으로 비교
            
            for str in strs[1:]: # 문자열마다 같은 인덱스를 비교함
                if compare != str[i]: # 같은 인덱스에 다른 문자가 있다면 결과 리턴
                    return answer
            
            answer += compare # 모두 같다면 answer 리스트에 해당 문자 추가
            
        return answer
