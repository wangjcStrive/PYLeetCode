# -*- coding: utf-8 -*-
# @Time    : 4/13/2018 2:40 PM
# @FileName: StringToInteger.py


# Info:
# 1. for i in range(len(s))
# 2. ord() -> get ascii index
# 3. can use regex


# all possible input:
# 1. whitespace character
# 2. not integer
# 3. int_max/int_min
# 4. negative integer!!!

import re


class Solution:

    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """
        str = str.strip()

        try:
            res = re.search('(^[\+\-]?\d+)', str).group()
            res = int(res)
            res = res if res <= 2147483647 else 2147483647
            res = res if res >= -2147483648 else -2147483648

        except:
            res = 0

        return res
