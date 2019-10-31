# https://leetcode.com/problems/remove-outermost-parentheses/

class Solution:
    def removeOuterParentheses(self, S: str) -> str:
        bal = 0
        result = ""
        
        for c in S:
            if c == '(':
                bal += 1
                if bal != 1:
                    result += c
                    
            if c == ')':
                bal -= 1
                if bal != 0:
                    result += c
        
        return result
