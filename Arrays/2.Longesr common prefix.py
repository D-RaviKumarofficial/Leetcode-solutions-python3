class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:

        # If no strings, return empty
        if not strs:
            return ""

        # Go through each position (0, 1, 2, 3...)
        for position in range(len(strs[0])):

            # Get the character at this position from first string
            char = strs[0][position]

            # Check this position in ALL other strings
            for i in range(1, len(strs)):
                
                # If this string is shorter, stop here
                if position >= len(strs[i]):
                    return strs[0][:position]
                
                # If character doesn't match, stop here
                if strs[i][position] != char:
                    return strs[0][:position]
        
        # If we checked everything, return the first string
        return strs[0]

        