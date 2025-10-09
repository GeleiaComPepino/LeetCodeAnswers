#
# @lc app=leetcode id=11 lang=python3
#
# [11] Container With Most Water
#

# @lc code=start
class Solution:
    def maxArea(self, height: List[int]) -> int:
        left = 0
        right = len(height) - 1
        max_water = 0
        while left < right:
            h = min(height[left], height[right])
            w = right-left
            area = h * w

            max_water = max(max_water, area)
            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return max_water
        
# @lc code=end

