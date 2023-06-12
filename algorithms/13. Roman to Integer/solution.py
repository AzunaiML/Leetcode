# https://leetcode.com/problems/roman-to-integer/

class Solution:
    # 1 <= s.length <= 15
    # s contains only the characters ('I', 'V', 'X', 'L', 'C', 'D', 'M').
    # It is guaranteed that s is a valid roman numeral in the range [1, 3999].
    def romanToInt(self, s: str) -> int:
        roman_int = {'I': 1,
                     'V': 5,
                     'X': 10,
                     'L': 50,
                     'C': 100,
                     'D': 500,
                     'M': 1000}

        result = 0
        prev = 0
        for c in reversed(s):
            cur = roman_int[c]
            if prev > cur:
                result -= cur
            else:
                result += cur
            prev = cur
        return result