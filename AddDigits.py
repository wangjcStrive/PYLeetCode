# -*- coding: utf-8 -*-
# @Time    : 5/21/2018 10:11 AM
# @FileName: AddDigits.py
# Info: input is 38, The process is like: 3 + 8 = 11, 1 + 1 = 2. Since 2 has only one digit, return it.

# digital root(数根)。用途
#    1. 检验计算正确性。比如两数字和的数根
#    2。 判断数字的整除性，如果数根能被3或9整除，则原来的数也能被3或9整除

class Solution:
    def addDigits(self, num):
        """
        :type num: int
        :rtype: int
        """
        while num//10>0:
            sum = 0
            while num%10>=0 and num!=0:
                sum += num%10
                num //= 10
            num = sum
        return num
