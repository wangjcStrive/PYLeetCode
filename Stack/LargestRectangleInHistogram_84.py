from typing import List

# 参照42. Trapping Rain Water。水池存水。

class LargestRectangleArea:
    def largestRectangleArea_LCode(self, heights: List[int]) -> int:
        size = len(heights)
        res = 0

        for i in range(size):
            left = i
            cur_height = heights[i]
            while left > 0 and heights[left - 1] >= cur_height:
                left -= 1

            right = i
            while right < size - 1 and heights[right + 1] >= cur_height:
                right += 1

            max_width = right - left + 1
            res = max(res, max_width * cur_height)
        return res


if __name__ == '__main__':
    ins = LargestRectangleArea()
    test_case = [1,1,2,1,1]
    result = ins.largestRectangleArea_LCode(test_case)
    print(result)