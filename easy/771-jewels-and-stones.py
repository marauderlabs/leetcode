# https://leetcode.com/problems/jewels-and-stones/

class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        jset = set(J)
        count = 0
        
        for s in S:
            if s in jset:
                count += 1
                
        return count
