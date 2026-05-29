class Solution:
    def minElement(self, nums: List[int]) -> int:
        res = float('inf')
        for num in nums:
            tmp = 0
            for ch in str(num):
                tmp += int(ch)
            res = min(res, tmp)
        return res