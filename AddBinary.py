# -*- coding: utf-8 -*-
# @Time    : 4/13/2018 4:16 PM
# @FileName: AddBinary.py
# Info:
# 1. eval() -> let a python program run python within itself. take string as a valid expression


class Solution:
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        # faster solution. slice
        # return bin(int(a, 2) + int(b, 2))[2:]

        return format(int(a, 2) + int(b, 2), 'b')
