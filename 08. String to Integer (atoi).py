class Solution:
    def myAtoi(self, s):
        i = 0
        n = len(s)
        sign = 1
        res = 0
        INT_MAX = 2147483647
        INT_MIN = -2147483648
        # bỏ khoảng trắng đầu
        while i < n and s[i] == ' ':
            i += 1
        # xét dấu
        if i < n and (s[i] == '+' or s[i] == '-'):
            if s[i] == '-':
                sign = -1
            i += 1
        # đọc số
        while i < n and s[i].isdigit():
            digit = ord(s[i]) - ord('0')
            if res > INT_MAX // 10 or (res == INT_MAX // 10 and digit > 7):
                return INT_MAX if sign == 1 else INT_MIN
            res = res * 10 + digit
            i += 1
        return sign * res
