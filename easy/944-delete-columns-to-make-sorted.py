# https://leetcode.com/problems/delete-columns-to-make-sorted/

class Solution:
    def minDeletionSize(self, A: List[str]) -> int:
        count = 0
        
        for col in zip(*A):
            for i in range(len(col)-1):
                if col[i] > col[i+1]:
                    count += 1
                    break
        
        return count
