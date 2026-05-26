from bisect import bisect_left, bisect_right
from math import isqrt
from typing import List

class Solution:
    def numberOfPairs(self, nums1: List[int], nums2: List[int], queries: List[List[int]]) -> List[int]:
        m = len(nums2)
        B = isqrt(m)                         # block size ≈ √m
        num_blocks = (m + B - 1) // B

        # True value of nums2[i] = nums2[i] + add[i // B]
        add = [0] * num_blocks
        blocks = []
        for b in range(num_blocks):
            lo, hi = b * B, min(b * B + B, m)
            blocks.append(sorted(nums2[lo:hi]))

        def range_update(l, r, val):
            for b in range(l // B, r // B + 1):
                lo, hi = b * B, min(b * B + B, m)
                if l <= lo and hi - 1 <= r:
                    # ✅ Full block: one number captures the whole update
                    add[b] += val
                else:
                    # ⚠️ Partial block: update individually and re-sort
                    for i in range(max(lo, l), min(hi, r + 1)):
                        nums2[i] += val
                    blocks[b] = sorted(nums2[lo:hi])

        def count_pairs(tot):
            ans = 0
            for v in nums1:                  # at most 5 iterations
                target = tot - v
                for b, block in enumerate(blocks):
                    # stored + add[b] == target  →  stored == target - add[b]
                    t = target - add[b]
                    ans += bisect_right(block, t) - bisect_left(block, t)
            return ans

        res = []
        for q in queries:
            if q[0] == 1:
                range_update(q[1], q[2], q[3])
            else:
                res.append(count_pairs(q[1]))
        return res