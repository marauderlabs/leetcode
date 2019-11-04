# https://leetcode.com/problems/unique-paths-ii/

class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid: List[List[int]]) -> int:
        rows = len(obstacleGrid)
        cols = len(obstacleGrid[0])
        
        paths = [[0]*cols for _ in range(rows)]
        
        # first row
        blocked = False
        for i in range(cols):
            if obstacleGrid[0][i] == 1:
                blocked = True
            if blocked:
                paths[0][i] = 0
            else:
                paths[0][i] = 1
        
        # first col
        blocked = False
        for i in range(rows):
            if obstacleGrid[i][0] == 1:
                blocked = True
            if blocked:
                paths[i][0] = 0
            else:
                paths[i][0] = 1
        
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            paths[0][0] = 1

        # other cells
        for i in range(1, rows):
            for j in range(1, cols):
                if obstacleGrid[i][j] == 1:
                    paths[i][j] = 0
                else:
                    paths[i][j] = paths[i-1][j] + paths[i][j-1]
        
        return paths[rows-1][cols-1]
