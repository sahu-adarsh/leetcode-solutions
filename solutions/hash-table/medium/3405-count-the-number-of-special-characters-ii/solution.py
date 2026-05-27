class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        last_lower = [-1] * 26
        first_upper = [float('inf')] * 26

        for i, ch in enumerate(word):
            if ch.islower():
                last_lower[ord(ch) - ord('a')] = i
            else:
                idx = ord(ch) - ord('A')
                first_upper[idx] = min(first_upper[idx], i)

        ans = 0
        for i in range(26):
            if last_lower[i] != -1 and first_upper[i] != float('inf'):
                if last_lower[i] < first_upper[i]:
                    ans += 1

        return ans