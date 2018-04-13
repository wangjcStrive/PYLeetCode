class Solution:
    # 1. Two sum
    # [3, 2, 4] -> [1, 2] not [0, 0]
    def two_sum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """
        if len(nums) <= 1:
            return False
        present = {}
        for i in range(len(nums)):
            if nums[i] in present:
                return i, present[nums[i]]
            else:
                present[target - nums[i]] = i
