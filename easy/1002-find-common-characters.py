# https://leetcode.com/problems/find-common-characters/submissions/
class Solution:
    def commonChars(self, A: List[str]) -> List[str]:
        c = collections.Counter(A[0])
        for a in A:
            cur = collections.Counter(a)
            for k, v in list(c.items()):
                if k in cur:
                    c[k] = min(c[k], cur[k])
                else:
                    del c[k]
            
        return list(c.elements())
