class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        n, m = len(matrix), len(matrix[0])
        i, j = 0, m-1

        while i<n and 0<=j:
            cur = matrix[i][j]

            if cur == target:
                return True
            if cur < target:
                i += 1
            else:
                j -= 1

        return False