class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        
        while left <= right:
            mid = (left + right) // 2  # Middle position
            
            if nums[mid] == target:  # Found!
                return mid
            elif nums[mid] < target:  # Go right
                left = mid + 1
            else:  # Go left
                right = mid - 1
        
        return left  # Position where it should be inserted
    