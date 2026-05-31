class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        PSE, NSE = [-1]*n, [n]*n
        stack = []

        for i, height in enumerate(heights):
            while stack and heights[stack[-1]] > height:
                NSE[stack.pop()] = i

            if stack:
                PSE[i] = stack[-1]
            
            stack.append(i)

        res = 0
        for i, height in enumerate(heights):
            res = max(res, (NSE[i] - PSE[i] - 1) * height)

        return res