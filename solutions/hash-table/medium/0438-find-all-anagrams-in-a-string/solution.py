from collections import defaultdict
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        n, m = len(s), len(p)
        mpp = defaultdict(int)
        mps = defaultdict(int)

        for ch in p:
            mpp[ch] += 1

        res = []
        have, want = 0, len(mpp)
        for i, ch in enumerate(s):
            mps[ch] += 1
            
            if mpp[ch] > 0 and mps[ch] == mpp[ch]:
                have += 1

                if have == want:
                    res.append(i-m+1)

            if (i-m+1) >= 0:
                if mps[s[i-m+1]] == mpp[s[i-m+1]]:
                    have -= 1
                mps[s[i-m+1]] -= 1

        return res