Given a sorted array of distinct integers and a target value, return the index if the target is found. 
If not, return the index where it would be if it were inserted in order.

You must write an algorithm with O(log n) runtime complexity.



class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left+right) // 2
            if nums[mid] > target: # target이 가운데 인덱스의 값보다 작으면 왼쪽 절반 탐색
                right = mid - 1
            elif nums[mid] < target: # target이 가운데 인덱스의 값보다 크면 오른쪽 절반 탐색
                left = mid + 1
            elif nums[mid] == target: # target 일치하면 return
                return mid
        
        return left # target이 없다면 left 값 리턴
