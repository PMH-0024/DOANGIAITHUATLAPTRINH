class Solution:
    def convert(self, s, numRows):
        if numRows == 1 or numRows >= len(s):
            return s
        rows = [""] * numRows
        cur = 0
        down = True
        for ch in s:
            rows[cur] += ch
            if cur == 0:
                down = True
            elif cur == numRows - 1:
                down = False
            cur += 1 if down else -1
        return "".join(rows)
