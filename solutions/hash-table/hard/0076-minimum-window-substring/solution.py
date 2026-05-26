from collections import defaultdict
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        mpt = defaultdict(int)
        mps = defaultdict(int)
        for ch in t:
            mpt[ch] += 1
        
        l, r = 0, 0
        n = len(s)
        res = [float('inf'), -1, -1]

        want, have = len(mpt), 0
        while l<=r and r<n:
            mps[s[r]] += 1

            if mpt[s[r]] > 0 and mps[s[r]] == mpt[s[r]]:
                have +=1
                while have == want:
                    if res[0] > (r-l+1):
                        res = [r-l+1, l, r]

                    if mpt[s[l]] > 0 and mps[s[l]] == mpt[s[l]]:
                        have -= 1
                    mps[s[l]] -= 1
                    l += 1
            
            r += 1

        if res[1] == -1:
            return ''
        return s[res[1] : res[2]+1]

            