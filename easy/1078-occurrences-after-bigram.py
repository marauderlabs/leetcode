# https://leetcode.com/problems/occurrences-after-bigram

class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        words = text.split()
        l = len(words)
        res = []
        for i, w in enumerate(words):
            if (w == first) and \
               (i+1 < l) and \
               (words[i+1] == second) and \
               (i+2 < l):
                res.append(words[i+2])
        
        return res
