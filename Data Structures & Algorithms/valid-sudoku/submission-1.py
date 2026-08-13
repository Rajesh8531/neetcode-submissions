class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        for i in range(len(board)):
            row = board[i][:]
            isDuplicate = self.containsDuplicatesInList(row)
            if isDuplicate:
                return False
        
        for i in range(len(board[0])):
            col = [row[i] for row in board]
            isDuplicate = self.containsDuplicatesInList(col)
            if isDuplicate:
                return False
        
        rowStart = 0
        rowEnd = rowStart + 2
        colStart = 0
        colEnd = colStart + 2
        while rowStart < len(board):
            while colStart < len(board[0]):
                isDuplicate = self.containDuplicates(rowStart,rowEnd,colStart,colEnd,board)
                if isDuplicate:
                    return False
                colStart = colEnd+1
                colEnd = colStart + 2
            colStart = 0
            colEnd = colStart + 2
            rowStart = rowEnd + 1
            rowEnd = rowStart + 2
        return True
        
    
    def containDuplicates(self,rowStart,rowEnd,colStart,colEnd,board):
        seen = set()
        for i in range(rowStart,rowEnd+1):
            for j in range(colStart,colEnd+1):
                num = board[i][j]
                if num in seen:
                    return True
                if num != '.':
                    seen.add(num)
        return False
    
    def containsDuplicatesInList(self,lst):
        seen = set()
        for num in lst:
            if num in seen:
                return True
            if num != '.':
                seen.add(num)
        return False