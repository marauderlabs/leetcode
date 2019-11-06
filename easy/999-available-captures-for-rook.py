# https://leetcode.com/problems/available-captures-for-rook

class Solution:
    def numRookCaptures(self, board: List[List[str]]) -> int:
        def getRookPosition(board: List[List[str]]) -> (int, int):
            for r, row in enumerate(board):
                for c, col in enumerate(row):
                    if col == 'R':
                        return r, c
        
        def countCapturedPawns(board: List[List[str]], row, col):
            count = 0

            # TODO: Refactor these directions into a loop

            r = row
            c = col
            # North
            while r >= 0 and board[r][c] != 'B':
                if board[r][c] == 'p':
                    count += 1
                    break
                r -= 1
            
            r = row
            c = col
            # South                    
            while r < 8 and board[r][c] != 'B':
                if board[r][c] == 'p':
                    count += 1
                    break
                
                r += 1
            
            r = row
            c = col
            # West
            while c >= 0 and board[r][c] != 'B':
                if board[r][c] == 'p':
                    count += 1
                    break
                c -= 1
            
            r = row
            c = col
            # East                    
            while c < 8 and board[r][c] != 'B':
                if board[r][c] == 'p':
                    count += 1
                    break
                
                c += 1
            
            return count
                
        
        r, c = getRookPosition(board)
        return countCapturedPawns(board, r, c)
