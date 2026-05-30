class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if k >= len(num):
            return '0'
        stack = []
        for ch in num:
            while k>0 and stack and stack[-1] > ch:
                stack.pop()
                k -= 1
            stack.append(ch)

        if k > 0:
            stack = stack[:-k]

        st = ''.join(str(i) for i in stack).lstrip('0')
        return '0' if not st else st