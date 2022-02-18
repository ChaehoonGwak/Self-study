Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

A subarray is a contiguous part of an array.



class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        dp = [0 for _ in range(len(nums))] # dp 초기화
        dp[0] = nums[0] # dp 초기값
        
        for idx, n in enumerate(nums[1:]):
            dp[idx+1] = max(dp[idx] + n, n) # 현재 n과 이전까지의 최대 연속합을 비교하여 dp에 삽입
            
        return max(dp) # 최대 연속합을 리턴
