# https://leetcode.com/problems/flipping-an-image/

class Solution:
    def flipAndInvertImage(self, A: List[List[int]]) -> List[List[int]]:
        for row in A:
            l = len(row)
            for i in range((len(row)+1)//2):
                row[i], row[-i-1] = row[-i-1]^1, row[i]^1
        return A
