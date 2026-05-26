class Solution:
    def passwordStrength(self, password: str) -> int:
        special = {'!', '@', '#', '$'}
        visited = set()
        res = 0

        for ch in password:
            if ch not in visited:
                visited.add(ch)
                
                if ch in special:
                    res += 5
                elif ord('a') <= ord(ch) <= ord('z'):
                    res += 1
                elif ord('A') <= ord(ch) <= ord('Z'):
                    res += 2
                elif ord('0') <= ord(ch) <= ord('9'):
                    res += 3

        return res