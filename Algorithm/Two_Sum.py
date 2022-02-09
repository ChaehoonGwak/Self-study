Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

You can return the answer in any order.



class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_index = {} # 수와 인덱스를 저장할 딕셔너리
        
        for idx, num in enumerate(nums):
            remainder = target - num # target에서 num을 뺀 나머지를 구함
            
            if remainder in num_index: # 딕셔너리에 나머지와 동일한 수가 있다면 해당 수의 인덱스와 현재 수의 인덱스 리스트로 리턴
                return [num_index[remainder], idx]
            num_index[num] = idx # 딕셔너리에 수와 인덱스 추가
