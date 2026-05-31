class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        n = len(matrix[0])
        res = 0
        graph = [0]*n
        for arr in matrix:
            for i, ele in enumerate(arr):
                if int(ele) == 0:
                    graph[i] = 0
                else:
                    graph[i] += int(ele)

            stack = []
            PSE, NSE = [-1]*n, [n]*n

            for i, ele in enumerate(graph):
                while stack and graph[stack[-1]] > ele:
                    NSE[stack.pop()] = i

                if stack:
                    PSE[i] = stack[-1]

                stack.append(i)

            for i, ele in enumerate(graph):
                res = max(res, (NSE[i] - PSE[i] - 1) * ele)

        return res