def decode_message(s: str, p: str) -> bool:
    x,y = len(s), len(p)
    dp = [[False] * (y + 1) for _ in range(x + 1)]
    dp[0][0] = True
    for j in range(1, y + 1):
        if p[j - 1] == '*':
            dp[0][j] = dp[0][j - 1]
    for i in range(1, x + 1):
        for j in range(1, y + 1):
            if p[j - 1] == '?':
                dp[i][j] = dp[i - 1][j - 1]
            elif p[j - 1] == '*':
                dp[i][j] = dp[i - 1][j] or dp[i][j - 1]
            else:
                dp[i][j] = dp[i - 1][j - 1] and s[i - 1] == p[j - 1]
    return dp[x][y]
