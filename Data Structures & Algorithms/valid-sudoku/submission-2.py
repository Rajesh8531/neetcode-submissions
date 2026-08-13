class Solution:
    def isValidSudoku(self, matrix: List[List[str]]) -> bool:
        rows = {}
        columns = {}
        squares = {}
        for row in range(len(matrix)):
            for col in range(len(matrix[0])):
                current_num = matrix[row][col]
                if current_num == '.':
                    continue
                if row not in rows:
                    rows[row] = set()
                if col not in columns:
                    columns[col] = set()
                square_row = row // 3
                square_col = col // 3
                key = f"{square_row}{square_col}"
                if key not in squares:
                    squares[key] = set()

                if current_num in rows[row]:
                    return False
                if current_num in columns[col]:
                    return False
                if current_num in squares[key]:
                    return False
                rows[row].add(current_num)
                columns[col].add(current_num)
                squares[key].add(current_num)
        return True
        