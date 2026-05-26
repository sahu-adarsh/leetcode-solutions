class Solution:
    def minOperations(self, nums: List[int]) -> int:
        n = len(nums)

        def solve(arr):
            z = arr.index(0)

            for i in range(n):
                if arr[(z + i) % n] != i:
                    return -1

            return z

        a = solve(nums)
        b = solve(nums[::-1])

        ans = float('inf')

        if a != -1:
            ans = min(ans, a, n - a + 2)

        if b != -1:
            ans = min(ans, b + 1, (n - b) % n + 1)

        return ans if ans != float('inf') else -1