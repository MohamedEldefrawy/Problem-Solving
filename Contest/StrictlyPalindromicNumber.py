# An integer n is strictly palindromic if, for every base b between 2 and n - 2 (inclusive), the string representation of the integer n in base b is palindromic.
#
# Given an integer n, return true if n is strictly palindromic and false otherwise.
#
# A string is palindromic if it reads the same forward and backward.

class Solution:
    def baseb(self, n, b):
        e = n // b
        q = n % b
        if n == 0:
            return '0'
        elif e == 0:
            return str(q)
        else:
            return self.baseb(e, b) + str(q)

    def is_palindromic(self, number, base):
        s = self.baseb(number, base)
        if ''.join(filter(str.isalnum, s)) == ''.join(filter(str.isalnum, s))[::-1]:
            return True
        return False

    def isStrictlyPalindromic(self, n: int) -> bool:
        i = 2
        while i <= n - 2:
            s = self.baseb(n, i)
            if not self.is_palindromic(n, i):
                return False
            i += 1
        return True


x = Solution()
print(x.isStrictlyPalindromic(4))
