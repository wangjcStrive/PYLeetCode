# -*- coding: utf-8 -*-
# @Time    : 5/22/2018 4:56 PM
# @FileName: fourSum.py
# Info: 18. 4Sum

class Solution:
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        listLen = len(nums)
        if listLen < 4:
            return []

        result = []
        # 先排序
        nums.sort()
        hashDict = {}
        i, j = 0, 1
        # 字典。 key是num[i]+nums[j], value是[i, j]
        for i in range(listLen):
            for j in range(i+1, listLen):
                tempSum = nums[i]+nums[j]
                if tempSum in hashDict:
                    hashDict[tempSum].append([i, j])
                else:
                    hashDict[tempSum] = [[i, j]]

        # 复杂度是O(n^2).两层循环
        for i in range(listLen-3):
            for j in range(i+1, listLen-2):
                gap = target-nums[i]-nums[j]
                if gap in hashDict:
                    for indexList in hashDict[gap]:
                        if j<indexList[0]:
                            tempList = list([i, j])
                            tempList.extend(indexList)
                            result.append([nums[i], nums[j], nums[indexList[0]], nums[indexList[1]]])
        nonDuplicateList = []
        for line in range(len(result)):
            if result[line] not in nonDuplicateList :
                nonDuplicateList.append(result[line])
        return nonDuplicateList

    def fourSum_fromLeetCode_more_faster(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        nums.sort()
        self.results = []

        def findNSum(nums, target, N, result):
            # print(result,nums,target)
            if len(nums) < N or target < nums[0] * N or target > nums[-1] * N:
                return
            if N == 2:
                l, h = 0, len(nums) - 1
                while l < h:
                    tmp = nums[l] + nums[h]
                    if tmp == target:
                        self.results.append(result + [nums[l], nums[h]])
                        l += 1
                        while l < h and nums[l] == nums[l - 1]: l += 1
                    elif tmp < target:
                        l += 1
                    else:
                        h -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if i == 0 or (i > 0 and nums[i] != nums[i - 1]):
                        findNSum(nums[i + 1:], target - nums[i], N - 1, result + [nums[i]])

        findNSum(nums, target, 4, [])
        return self.results


if __name__ == '__main__':
    myIns = Solution()
    inputList = [-3, -2, -1, 0, 0, 1, 2, 3]
    output = myIns.fourSum(inputList, 0)
    print(output)
