class Solution:
    def countValidSubsets(self, parent: List[int], nums: List[int], k: int) -> int:
        MOD = 10**9 + 7
        n = len(parent)
        
        children = [[] for _ in range(n)]
        for i in range(1, n):
            children[parent[i]].append(i)
        
        order = []
        stack = [0]
        while stack:
            v = stack.pop()
            order.append(v)
            for c in children[v]:
                stack.append(c)
        
        dp = [[[0] * k for _ in range(2)] for _ in range(n)]
        
        for v in reversed(order):   # process leaves first
            dp[v][0][0] = 1                     # v not selected
            dp[v][1][nums[v] % k] = 1           # v selected
            
            for c in children[v]:
                new_dp = [[0] * k for _ in range(2)]
                
                for r1 in range(k):
                    if dp[v][0][r1]:
                        for r2 in range(k):
                            r = (r1 + r2) % k
                            new_dp[0][r] = (new_dp[0][r] +
                                dp[v][0][r1] * (dp[c][0][r2] + dp[c][1][r2])) % MOD
                    
                    if dp[v][1][r1]:
                        for r2 in range(k):
                            r = (r1 + r2) % k
                            new_dp[1][r] = (new_dp[1][r] +
                                dp[v][1][r1] * dp[c][0][r2]) % MOD
                
                dp[v] = new_dp
        
        return (dp[0][0][0] + dp[0][1][0] - 1) % MOD