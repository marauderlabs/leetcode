# https://leetcode.com/problems/to-lower-case

class Solution:
    def toLowerCase(self, str: str) -> str:
        s = ""
        for c in str:
            if c >='A' and c <= 'Z':
                c = chr(ord('a') + ord(c) - ord('A'))
            s += c
        return s
