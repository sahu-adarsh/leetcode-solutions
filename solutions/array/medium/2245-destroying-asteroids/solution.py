class Solution:
    def asteroidsDestroyed(self, mass: int, asteroids: List[int]) -> bool:
        MAX_VAL = 100000
        freq = [0] * (MAX_VAL + 1)

        xmin, xmax = MAX_VAL, 0

        for x in asteroids:
            freq[x] += 1
            xmin = min(xmin, x)
            xmax = max(xmax, x)

        planet = mass

        for x in range(xmin, xmax + 1):
            if freq[x] == 0:
                continue

            if x > planet:
                return False

            planet += x * freq[x]

        return True