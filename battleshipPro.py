class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        row, col = len(board), len(board[0])
        for i in range(row):
            for j in range(col):
                if i > 0 and board[i - 1][j] == 'X': continue
                if j != col - 1 and board[i][j] == 'X' and board[i][j + 1] != 'X' or j == col - 1 and board[i][j] == 'X':
                    count += 1
        return count

if __name__ == '__main__':
    obj = Solution()
    # c = obj.countBattleships([[s for s in 'X..X'],[s for s in '...X'],[s for s in '...X']])
    c = obj.countBattleships([[s for s in '.']])
    print(c)