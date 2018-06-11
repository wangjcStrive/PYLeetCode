# -*- coding: utf-8 -*-
# @Time    : 5/22/2018 9:02 AM
# @FileName: LongestSubstringWithoutRepeatingCharacters.py
# Info: LCode 3.
# solution: Hash


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        head = 0
        dic = {}
        res = 0
        for i in range(len(s)):
            if s[i] in dic and dic[s[i]] >= head:
                res = max(res, i-head)
                head = dic[s[i]]+1
            dic[s[i]] = i
        return max(res, len(s)-head)

if __name__ == '__main__':
    input = ['aa', 'abcabcbb', 'pwwkew']
    myInstance = Solution()
    for x in input:
        print(myInstance.lengthOfLongestSubstring(x))