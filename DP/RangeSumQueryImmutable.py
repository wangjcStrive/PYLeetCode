# -*- coding: utf-8 -*-
# @Time    : 8/14/2018 10:36 AM
# @FileName: RangeSumQueryImmutable.py
# Info: 303. Range Sum Query - Immutable

# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(i,j)

class NumArray:

    def __init__(self, nums):
        """
        :type nums: List[int]
        """
        self.num = nums
        self.DP = [0] * len(nums)

    # need long time version
    def sumRange(self, i, j):
        """
        :type i: int
        :type j: int
        :rtype: int
        """
        return sum(self.num[i:j+1])

    # DP version: DP[i] 表示从0~i的加和，则[i, j] = DP[j]-DP[i]
    def sumRangeDP(self, i, j):
        self.DP[0] = self.num[0]
        for i in range(1, len(self.num)):
            self.DP[i] = self.DP[i-1]+self.num[i]

        return self.DP[j]-self.DP[i-1]

if __name__ == '__main__':
    ins = NumArray([1, 2, 3, 4])
    print(ins.sumRangeDP(1, 3))
    print(ins.DP)