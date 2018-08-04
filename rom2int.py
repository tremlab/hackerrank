# https://leetcode.com/problems/roman-to-integer/description/
# Friends!  Romans!  Integers!

class Solution:
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        'IX' = 9
        'XI' = 11
        """
        int_vals = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }

        int_result = 0

        prev = 0

        for c in s:
            int_c = int_vals[c]

            if int_c > prev:
                int_result = int_result - prev
            else:
                int_result = int_result + prev

            prev = int_c

        int_result = int_result + prev

        return int_result
