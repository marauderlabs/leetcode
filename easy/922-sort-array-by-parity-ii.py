# https://leetcode.com/problems/sort-array-by-parity-ii/

class Solution:
    def sortArrayByParityII(self, A: List[int]) -> List[int]:
        # find an even number and put it at this position, if it's not.

        e = 1 #possible wrongly placed even number position
        for i in range(0, len(A), 2):
            if A[i] % 2 != 0:
                while A[e] % 2 != 0:
                    e += 2
                A[e], A[i] = A[i], A[e]

        return A
