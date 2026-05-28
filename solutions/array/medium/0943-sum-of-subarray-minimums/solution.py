class Solution:
    def sumSubarrayMins(self, arr: List[int]) -> int:
        n = len(arr)
        PSE, NSE = [-1]*n, [n]*n

        stack = []
        for i in range(n):
            while stack and arr[stack[-1]] >= arr[i]:
                top = stack.pop()
                NSE[top] = i

            if stack:
                PSE[i] = stack[-1]

            stack.append(i)

        # stack = []
        # for i in range(n-1, -1, -1):
        #     while stack and arr[stack[-1]] > arr[i]:
        #         stack.pop()
            
        #     if stack:
        #         NSE[i] = stack[-1]

        #     stack.append(i)

        res = 0
        mod = int(1e9 + 7)
        for i, num in enumerate(arr):
            left = i - PSE[i]
            right = NSE[i] - i
            res += (left * right * num)
            res %= mod

        return res



            