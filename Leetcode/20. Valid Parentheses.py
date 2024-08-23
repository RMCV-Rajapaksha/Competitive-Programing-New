class Solution:
    def isValid(self, s: str) -> bool:
 
        matching_brackets = {')': '(', '}': '{', ']': '['}

        stack = []
        
 
        for char in s:
            if char in matching_brackets:
           
                top_element = stack.pop() if stack else '#'
                if matching_brackets[char] != top_element:
                    return False
            else:

                stack.append(char)

        return not stack
