class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # Create an empty dictionary (memory book) to remember numbers we've seen
        seen = {}

        # Go through each number in the list one by one
        for i , num in enumerate(nums):
            # Print what loop turn we're on and what number we're looking at
            print(f"loop turn i:{i}, num : {num}")

            # Calculate what number we need to find to reach the target
            needed = target - num
            # Print what number we're looking for
            print(f"we need num : {needed}")

            # Check: Did we already see this needed number in our memory?
            if needed in seen:
                # YES! We found it! Return the positions of both numbers
                return [seen[needed], i]
            
            # NO? Then remember this number and remember which position it was at
            seen[num] = i