# -*- coding: utf-8 -*-
# @Time    : 7/30/2018 6:37 PM
# @FileName: LIS.py
# Info:

# input:  4 1 2 3 6 5 8 7 -> 1 2 3 5 7
# F(i) = 1 + max( F(1), F(2)... F(i-1))

# 从前往后，F(i) = 1 + max( F(j) ). 其中的j要满足nums[j] < num[i]

import bisect

def LIS(nums):
    """
    :param nums:
    :return: LIS
    """
    length = len(nums)
    if length == 0:
        return 0
    LISList = [0] * length
    LISList[0] = 1
    for i in range(1, length):
        tempLongest = 0
        for j in range(0, i):
            if nums[j] < nums[i]:
                if tempLongest < LISList[j]:
                    tempLongest = LISList[j]
        LISList[i] = tempLongest + 1
    print(LISList)
    return max(LISList)


def LISFromLeetcode(nums):
    """
    :type nums: List[int]
    :rtype: int
    """
    if not nums:
        return 0
    dp = []
    for i in nums:
        idx = bisect.bisect_left(dp, i)
        if len(dp) == idx:
            dp += [i]
        else:
            dp[idx] = i
    return len(dp)



if __name__ == '__main__':
    # input = [4, 1, 2, 3, 6, 4, 5, 8, 7]
    input = [1,3,6,7,9,4,10,5,6]
    print(LIS(input))
    print(LISFromLeetcode(input))
