# https://leetcode.com/problems/climbing-stairs/

class Solution:
    def climbStairs(self, n: int) -> int:

        # Bottom Up with O(n) space
        cache = [None] * (n+1)
        def helperBU(n: int):
            if n < 0:
                return 0
            if n == 0:
                return 1
            if cache[n] is not None:
                return cache[n]
                
            cache[n] = helper(n-1) + helper(n-2)
            return cache[n]
        
    
        # Top Down with O(1) space
        def helperTD(n: int):
            dp1 = 1
            dp2 = 1
            if n < 2:
                return 1
            for _ in range(1, n):
                result = dp1 + dp2
                dp1 = dp2
                dp2 = result
            return result
                
        return helperTD(n)
