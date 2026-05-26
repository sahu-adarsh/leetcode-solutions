from collections import defaultdict
class Solution:
    def maxJumps(self, arr: List[int], d: int) -> int:
        adj = defaultdict(list)
        n = len(arr)

        for i in range(n):
            for j in range(i+1, min(i+d+1, n)):
                if arr[i] <= arr[j]:
                    break
                adj[i].append(j)

            for j in range(i-1, max(i-d-1, -1), -1):
                if arr[i] <= arr[j]:
                    break
                adj[i].append(j)

        def solve(i):
            if not adj[i]:
                return 1
            if i in dp:
                return dp[i]

            dp[i] = 1 + max(solve(nei) for nei in adj[i])
            return dp[i]

        dp = {}
        return max(solve(i) for i in range(n))
