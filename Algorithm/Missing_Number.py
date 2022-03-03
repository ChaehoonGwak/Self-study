Given an array nums containing n distinct numbers in the range [0, n], return the only number in the range that is missing from the array.

Constraints:
n == nums.length
1 <= n <= 10**4
0 <= nums[i] <= n
All the numbers of nums are unique.



class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        complete_sum = (len(nums) * (len(nums) + 1)) // 2 # 빠진 수가 없을 때 수열의 합
        sum_nums = sum(nums) # 빠진 수가 있을 때 수열의 합
        
        return complete_sum - sum_nums
