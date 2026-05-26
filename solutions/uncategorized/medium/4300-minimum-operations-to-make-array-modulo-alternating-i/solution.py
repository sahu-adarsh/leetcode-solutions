class Solution:
    def minOperations(self, nums: list[int], k: int) -> int:
        res = float('inf')
        for i in range(0,k):
            for j in range(0,k):
                if i==j: continue
                tmp = 0
                for l, num in enumerate(nums):
                    target = num % k
                    if l%2 == 0:
                        diff = abs(target-i)
                    else:
                        diff = abs(target-j)
                    tmp += min(diff, k-diff)

                res = min(res, tmp)

        return res