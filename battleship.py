class Solution(object):
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        rows = len(board)
        cols = len(board[0])
        visited = [[0 for _ in range(cols)] for _ in range(rows)]
        i, j = 0, 0
        sum = 0
        while i < rows or j < cols:
            if visited[i][j] ==0 and board[i][j] == 'X':
                sum += 1
                visitShip(board, i, j, visited)
            visited[i][j] = 1
            i,j=move(i,j,rows,cols,visited)
            if i == rows-1 and j == cols -1 and visited[i][j] == 1:
                break
        return sum

def move(i, j, r, c, visited):
    if j == c-1 and i == r-1:#保证第一步开始时不是最后一行的最后一列
        return i,j
    j = j+1 if j < c-1 else 0#所以这里可以默认允许换行
    i = i if j > 0 else i + 1
    while visited[i][j] == 1:
        j = j + 1 if j < c - 1 else (0 if i < r-1 else j) #判断是否可以换行，若不能换行则保持j不变
        i = i if j > 0 else i + 1 #j已经判断过是否可以换行，这里可以不再做判断
        if j == c-1 and i == r-1:#走到最后一位就break
            break
    return i,j

def visitShip(board, i, j, visited):
    r,c = len(board),len(board[0])
    if i == r-1 and j == c-1: #保证当前不在最后一位
        return
    down,right = i+1,j+1
    vertical = 1 if right == c else (0 if board[i][right]=='X' else 1)
    if vertical:
        while down < r and board[down][j] == 'X':
            visited[down][j] = 1
            down += 1
    else:
        while right < c and board[i][right] == 'X':
            visited[i][right] = 1
            right += 1

if __name__ == '__main__':
    m = [[s for s in '.']]
    obj = Solution()
    sum = obj.countBattleships(m)
    print(sum)