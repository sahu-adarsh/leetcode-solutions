class Solution:
    def numberOfSpecialChars(self, word: str) -> int:
        lower = set(ch for ch in word if ch.islower())
        upper = set(ch.lower() for ch in word if ch.isupper())
        return len(lower & upper)