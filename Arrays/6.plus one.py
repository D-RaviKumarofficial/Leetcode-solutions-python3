class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        n = len(digits)
        
        # Start from the last digit and move towards the first
        for i in range(n - 1, -1, -1):
            if digits[i] < 9:  # If the digit is less than 9, just increment it
                digits[i] += 1
                return digits
            else:  # If the digit is 9, set it to 0 and continue to the next digit
                digits[i] = 0
        
        # If all digits were 9, we need to add a new digit at the front
        return [1] + digits