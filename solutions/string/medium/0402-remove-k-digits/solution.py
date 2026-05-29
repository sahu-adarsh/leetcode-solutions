class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        tmp = []
        a = k
        stack = []
        for ch in num:
            while a>0 and stack and stack[-1] > int(ch):
                stack.pop()
                a -= 1
            stack.append(int(ch))

        if a > 0:
            stack = stack[:len(stack)-a]

        if not stack:
            return '0'

        j = 0
        while stack and j < len(stack) and stack[j] == 0:
            j += 1

        st = ''.join(str(i) for i in stack[j:])
        if st == '':
            return '0'
        return st