class Solution:
    def isSafePlace(self, board, row, col, board_len):
        row_place_holder = row
        col_place_holder = col

        #Check the upper diagonal
        while row >= 0 and col >= 0:
            if board[row][col] == 'Q':
                return False
            row -= 1
            col -= 1
        
        #Check the horizontal left direction
        row = row_place_holder
        col = col_place_holder

        for col_ind in range(col, -1, -1):
            if board[row][col_ind] == 'Q':
                return False
        
        #Check lower diagonal
        row = row_place_holder
        col = col_place_holder

        while row < board_len and col >= 0:
            if board[row][col] == 'Q':
                return False
            row += 1
            col -= 1
        
        return True


    def solve(self, answer_array, board, board_len, col):
        if col == board_len:
            answer_array.append(list(board))
            return
        
        for row in range(board_len):
            if self.isSafePlace(board, row, col, board_len):
                board[row] = board[row][:col] + 'Q' + board[row][col+1:]
                self.solve(answer_array, board, board_len, col+1)
                board[row] = board[row][:col] + '.' + board[row][col+1:]


    def solveNQueens(self, n: int) -> List[List[str]]:
        answer_array = []
        chess_board = ['.' * n for ind in range(n)]
        self.solve(answer_array, chess_board, n, 0)
        return answer_array