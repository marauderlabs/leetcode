# https://leetcode.com/problems/matrix-cells-in-distance-order

class Solution:
    def allCellsDistOrder(self, R: int, C: int, r0: int, c0: int) -> List[List[int]]:
        matrix = []
        for r in range(R):
            matrix.extend([[r, c] for c in range(C)])
        
        return sorted(matrix, key = lambda cell: abs(cell[0]-r0) + abs(cell[1]-c0))
