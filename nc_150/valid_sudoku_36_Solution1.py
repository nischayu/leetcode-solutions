class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        

        #For each row in the sudoku table
            #do a count duplicates, if duplicate found, return false
        #^CORRECT
        #For each column in the sudoku table
            #do a count duplicates, if duplicate found, return false
        #^CORRECT

        #For each 3x3 square in the sudoku table
            #do a count duplicates, if duplicate found return false
        #^ALMOST CORRECT, just need to divide grid indices into 3x3 format
        #return True


        #This program is incorrect
        
        #rows
        for i in range(0, len(board)):
            rowSet = {}
            for j in range(0, len(board[i])):
                if(board[i][j] == "."):
                    continue
                if(board[i][j] not in rowSet.keys()):
                    rowSet[board[i][j]] = 1
                else:
                    return False
            
        #columns
        for i in range(0, len(board)):
            colSet = {}
            for j in range(0, len(board[i])):
                if(board[j][i] == "."):
                    continue
                if(board[j][i] not in rowSet.keys()):
                    rowSet[board[j][i]] = 1
                else:
                    return False
        
        #3x3 grid
        gridSet = {}
        for i in range(0, len(board)):
            for j in range(0, len(board[i])):
                if(board[i][j] == "."):
                    continue
                gridR = int(i/3)
                gridC = int(j/3)
                gridSet[(gridR,gridC)] = 1 +