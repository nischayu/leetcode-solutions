class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        
        rows = collections.defaultdict(set)
        cols = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for i in range(0, 9):
            for j in range(0, 9):
                if(board[i][j] == "."):
                    continue
                if(board[i][j] in rows[i]):
                    return False
                elif(board[i][j] in cols[j]):
                    return False
                elif(board[i][j] in squares[(int(i/3), int(j/3))]):
                    return False

                rows[i].add(board[i][j])
                cols[j].add(board[i][j])
                squares[(int(i/3), int(j/3))].add(board[i][j])

        return True

        #The time complexity of this solution is O(9^2)
        #The space complexity of this solution is O(3 * 9^2) = O(3^5)