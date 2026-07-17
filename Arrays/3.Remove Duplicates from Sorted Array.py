def removeDuplicates(nums):
    # Check if array is empty, return 0 if true
    if not nums:
        return 0
    
    # Pointer that tracks where next unique element should go
    unique_idx = 0
    
    # Loop through array starting from index 1 (second element)
    for i in range(1, len(nums)):
        # Check if current element is different from element at unique_idx
        if nums[i] != nums[unique_idx]:
            # Move unique pointer to next position
            unique_idx += 1
            # Place current unique element at unique_idx position
            nums[unique_idx] = nums[i]
    
    # Return count of unique elements (unique_idx + 1 because indexing starts at 0)
    return unique_idx + 1