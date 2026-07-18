class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        # Pointer to track the position of the next element that is not equal to val
        insert_pos = 0
        
        # Loop through each number in the list
        for num in nums:
            # If the current number is not equal to val, we want to keep it
            if num != val:
                # Place it at the insert position and move the insert position forward
                nums[insert_pos] = num
                insert_pos += 1
        
        # Return the new length of the array after removing all instances of val
        return insert_pos