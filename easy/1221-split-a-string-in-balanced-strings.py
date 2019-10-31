# https://leetcode.com/problems/split-a-string-in-balanced-strings

class Solution:
    def balancedStringSplit(self, s: str) -> int:
        bal = 0
        count = 0

        for c in s:
            if c == 'L':
                bal += 1
            else:
                bal -= 1

            if bal == 0:
                count +=1

        return count
