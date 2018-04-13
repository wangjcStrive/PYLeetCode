# -*- coding: utf-8 -*-
# @Time    : 3/27/2018 10:05 AM
# @FileName: ReverseInteger.py
# Info:

# 123 -> 321
# 120 -> 21
# -123 -> -321
# Assume we are dealing with an environment which could only hold
# integers within the 32-bit signed integer range. For the purpose
# of this problem, assume that your function returns 0 when the reversed integer overflows.
# 1534236469 -> should be 0


class Solution:
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """
        length = 0
        result = 0
        allBit = []
        isNegative = False
        if x < 0:
            x = abs(x)
            isNegative = True
        while x != 0 or x % 10 != 0:
            allBit.append(x % 10)
            length += 1
            x //= 10

        for i in allBit:
            result += i * (10 ** (length - 1))
            length -= 1

        if result > 2147483648:
            return 0
        else:
            return isNegative and -result or result

    # from website, faster function
    def reverse_others(self, x):
        """
        :type x: int
        :rtype: int
        """
        if x >= 0:
            flag = 1
        else:
            flag = -1
            x = -x
        new_x = 0
        while x:
            new_x = new_x * 10 + x % 10
            x //= 10
        new_x = flag * new_x
        if 2 ** 31 - 1 > new_x >= -2 ** 31:
            return new_x
        else:
            return 0
