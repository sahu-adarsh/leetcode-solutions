class Solution:
    def minimumSwaps(self, nums: list[int]) -> int:
        count = 0
        n = len(nums)

        for num in nums:
            if num == 0:
                count += 1

        if count == 0:
            return 0
        
        res = 0
        for i, num in enumerate(nums[::-1]):
            count -= 1
            if num != 0:
                res += 1
            if count == 0:
                break

        return res