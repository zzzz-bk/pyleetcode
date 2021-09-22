class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        m,n = len(s),len(p)
        dp = [[False] * (n+1) for _ in range(m+1)]
        dp[0][0] = True
        def match(i,j):
            if i==0:
                return True
            elif p[j-1] == '.':
                return True
            return s[i-1] == p[j-1]
        for i in range(m+1):
            for j in range(1,n+1):                #i,j 在dp中代表s,p的长度
                if p[j-1] == '*':
                    dp[i][j] |= dp[i][j-2]        #字母+‘*’号没有与s[i]匹配
                    if match(i,j-1):
                        dp[i][j] |= dp[i-1][j]    #*号前的字母与s[i]匹配了,这种情况与去掉s[i]的匹配情况相等
                else:
                    if match(i,j):
                        dp[i][j] |= dp[i-1][j-1]
        return dp[m][n]