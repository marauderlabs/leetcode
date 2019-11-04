# https://leetcode.com/problems/generate-parentheses/

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        strings: List[str] = []
        
        def helper(left: int, right: int, string) -> None:
            if left == 0 and right == 0:
                strings.append(string)
                return
                        
            if left != 0:                
                helper(left-1, right, string+'(')
            if right > left:
                helper(left, right-1, string+')')
                
        helper(n, n, "")
        return strings
