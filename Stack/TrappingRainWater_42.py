from typing import List
import time

def show_time():
    print(time.time())

class Solution:
    def trap_1(self, height: List[int]) -> int:
        """
        往两边找，两边要都比当前位置高，那么当前位置就能存水.
        O(n^2)?
        :param height:
        :return:
        """
        result = 0
        for i in range(1, len(height)):
            curr_value = height[i]
            left_max = 0
            right_max = 0
            # 这里效率低，每个点都要从当前位置往两边走一遍，找出两边的最大值
            for j in range(0, i):
                if height[j] > left_max:
                    left_max = height[j]
            for k in range(i, len(height)):
                if height[k] > right_max:
                    right_max = height[k]
            if left_max > curr_value and right_max > curr_value:
                result = result + min(left_max, right_max) - curr_value
        return result

    # 想到的一个方法， 但是没有trap_1里的复杂度低。记录两边的最大值及其位置left_max(maxValue, index)/ right_max(maxValue, index)，当越过位置后再更新
    # def trap(self, height: List[int]) -> int:
    def trap_2(self, height: List[int]) -> int:
        """
        DP
        trap1()中，计算两边的最大值，每次都要重新遍历一遍所有高度，可以优化一下
		先从左边遍历一遍，计算每个位置上的左边的最大值，更新到vector maxLeft.
		再从右边往左边遍历一遍，计算每个位置上右边的最大值，更新到vector maxRight;
		然后再遍历一遍就好了
		时间复杂度：O(3n)
		空间复杂度：O(2n)
        :param height:
        :return:
        """
        result = 0
        length = len(height)
        left_max_list = [0] * length
        maxLeftValue = height[0]
        for i in range(1, length):
            if height[i - 1] > maxLeftValue:
                maxLeftValue = height[i - 1]
            left_max_list[i] = maxLeftValue

        right_max_list = [0] * length
        maxRightValue = height[-1]
        for i in range(length - 2, -1, -1):
            if height[i + 1] > maxRightValue:
                maxRightValue = height[i + 1]
            right_max_list[i] = maxRightValue

        for i in range(1, length):
            if height[i] < left_max_list[i] and height[i] < right_max_list[i]:
                result = result + min(left_max_list[i], right_max_list[i]) - height[i]

        return result

    def trap_3(self, height: List[int]) -> int:
        """
        双指针
        在DP中，往往可以对"空间"复杂度进一步优化
        max_left [ current ] 和 max_right [ current ] 数组中的元素我们其实只用一次，然后就再也不会用到了。所以我们可以不用数组，只用一个元素就行了
        用两个指针(index)记录两边的最大值
        这种解法也不需要trap_2里面的提前先走两趟，记录每个位置的左右最大值，更快!
        :param height:
        :return:
        """
        result = 0
        length = len(height)
        if length == 0:
            return result

        left_max_index = 0
        right_max_index = length - 1
        for i in range(1, length):
            if height[left_max_index] < height[right_max_index]:
                if height[i-1]>height[left_max_index]:
                    left_max_index = i
                if height[i] < height[left_max_index]:
                    result = result + height[left_max_index] - height[i]
            else:
                if height[i]>height[right_max_index]:
                    right_max_index = i
                if height[i] < height[right_max_index]:
                    result = result + height[right_max_index]-height[i]
        print(result)
        return result

if __name__ == '__main__':
    waterList = [0, 7, 0, 2, 1, 0, 1, 5, 2, 1, 2, 1]
    ins = Solution()
    print(ins.trap_1(waterList))
    print(ins.trap_2(waterList))
    print(ins.trap_3(waterList))
