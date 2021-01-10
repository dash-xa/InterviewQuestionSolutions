class Solution:
    def __init__(self):
        self.board = None
        self.R = self.C = -1
        self.W = -1
        
    def _search(self, r, c, word, d):
        """Find if word exists in grid with starting index at (row, col)"""
        if self.board[r][c] != word[d]:
            return False        
        if d == self.W - 1:
            return True
        val, self.board[r][c] = self.board[r][c], "*"
        for i, j in [(r - 1, c), (r + 1, c), (r, c - 1), (r, c + 1)]:
            if (0 <= i < self.R and 0 <= j < self.C) and self._search(i, j, word, d + 1):
                return True
        self.board[r][c] = val
        return False
    
    def exist(self, board, word):
        self.board = board
        self.R, self.C = len(board), len(board[0])
        self.W = len(word)
        for r in range(self.R):
            for c in range(self.C):
                if self._search(r, c, word, 0):
                    return True
        return False