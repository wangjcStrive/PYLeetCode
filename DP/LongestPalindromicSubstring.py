# -*- coding: utf-8 -*-
# @Time    : 8/3/2018 9:40 AM
# @FileName: LongestPalindromicSubstring.py
# Info: 5. Longest Palindromic Substring


# DP: p[i][j]表示以i开始到j结束的范围内是否是回文，则:
# p[i][j] = (s[i]==s[j]) && p[i+1][j-1]==true?

class Solution:

    # DP. O(n^2)
    # 两层循环 + 状态存储
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        strLength = len(s)
        left = right = 0
        palindromicLen = 0
        DP = [[-1 for i in range(strLength)] for i in range(strLength)]
        for i in range(strLength):
            DP[i][i] = True
        for j in range(strLength):
            i = 0
            for i in range(j):
                DP[i][j] = ( (s[i] == s[j]) and (DP[i + 1][j - 1] or j - i < 2) )
                if DP[i][j] and palindromicLen < j - i + 1:
                    palindromicLen = j - i + 1
                    left = i
                    right = j
        return s[left:right+1]

    # O(n)
    def longestPalindrome_Manache(self, s):
        pass

if __name__ == '__main__':
    ins =  Solution()
    print(ins.longestPalindrome('a'))
