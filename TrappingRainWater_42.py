class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        sum=0
        stack = []
        stack.add(height[0])
        for i in range(1, len(height)):
            if height[i]<stack[-1]:
                stack.add(height[i])
            else:
                sum = sum + calculateWaterInStack(stack)


    def calculateWaterInStack(stack):
        
        return water;