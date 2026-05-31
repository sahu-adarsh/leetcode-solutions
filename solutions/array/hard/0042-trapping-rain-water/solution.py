class Solution:
    def trap(self, height: List[int]) -> int:
        stack = []
        res = 0

        for i, h in enumerate(height):
            while stack and height[stack[-1]] < h:
                bottom = stack.pop()

                if not stack:
                    break

                l = stack[-1]
                width = i - l - 1
                res += (min(height[i], height[l]) - height[bottom]) * width

            stack.append(i)

        return res