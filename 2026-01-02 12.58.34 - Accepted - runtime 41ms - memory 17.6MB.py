class Solution:
    def isValid(self, s: str) -> bool:
        # Use stack - whenever we see 'c', check if last two chars are 'ab'
        stack = []
        
        for c in s:
            stack.append(c)
            
            # Check if last 3 chars are "abc"
            if len(stack) >= 3 and stack[-3:] == ['a', 'b', 'c']:
                stack.pop()
                stack.pop()
                stack.pop()
        
        return len(stack) == 0