from collections import defaultdict
class Solution:
    def limitOccurrences(self, nums: list[int], k: int) -> list[int]:
        mp = defaultdict(int)
        res = []

        for num in nums:
            mp[num] += 1
            if mp[num] <= k:
                res.append(num)

        return res