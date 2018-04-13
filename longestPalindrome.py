# 5. Longest Palindromic Substring
# [1, 1, 2] -> [1, 1]
# [1, 1, 1] -> [1, 1, 1]  ****


class Solution:

    def get_palindrome(self, s, left_index, right_index):
        result = str()
        while left_index >= 0 and right_index < len(s):
            if s[left_index] == s[right_index]:
                left_index -= 1
                right_index += 1
            else:
                break
        result = s[left_index + 1:right_index]
        return result, len(result)

    def longest_palindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if len(s) < 2:
            return s
        maxLen = 0
        resultStr = str()
        for i in range(0, len(s) - 1):
            if s[i] == s[i + 1]:
                subStr_mid, strLen_mid = self.get_palindrome(s, i, i + 1)
                subStr_right, strLen_right = self.get_palindrome(s, i, i)
                subStr = (strLen_mid > strLen_right) and subStr_mid or subStr_right
                strLen = len(subStr)
            else:
                subStr, strLen = self.get_palindrome(s, i, i)
            if strLen > maxLen:
                maxLen = strLen
                resultStr = subStr
        return resultStr


# faster solution
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        maxLen = 1
        start = 0
        for i in range(len(s)):
            if i - maxLen >= 1 and s[i - maxLen - 1:i + 1] == s[i - maxLen - 1:i + 1][::-1]:
                start = i - maxLen - 1
                maxLen += 2
                continue

            if i - maxLen >= 0 and s[i - maxLen:i + 1] == s[i - maxLen:i + 1][::-1]:
                start = i - maxLen
                maxLen += 1
        return s[start:start + maxLen]
