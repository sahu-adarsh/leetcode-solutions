from functools import cache
class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        if s[0] != '0' or s[n-1] != '0':
            return False

        dp = [False]*n
        dp[0] = True
        pre = [0]*(n+1)
        pre[1] = 1

        for i in range(1, n):
            if s[i] == '0':
                hi = i - minJump
                lo = max(0, i - maxJump)

                if hi >= 0 and pre[hi+1] - pre[lo] > 0:
                    dp[i] = True

            pre[i+1] = pre[i] + dp[i]

        return dp[n-1]