#
# @lc app=leetcode id=4 lang=python3
#
# [4] Median of Two Sorted Arrays
#

# @lc code=start
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1

        m, n = len(nums1), len(nums2)
        left, right = 0, m

        while left <= right:
            i = (left + right) // 2
            j = (m + n + 1) // 2 - i

            nums1Left = nums1[i - 1] if i > 0 else float("-inf")
            nums1Right = nums1[i] if i < m else float("inf")
            nums2Left = nums2[j - 1] if j > 0 else float("-inf")
            nums2Right = nums2[j] if j < n else float("inf")

            if nums1Left <= nums2Right and nums2Left <= nums1Right:
                if (m + n) % 2 == 0:
                    return (max(nums1Left, nums2Left) + min(nums1Right, nums2Right)) / 2
                else:
                    return max(nums1Left, nums2Left)
            elif nums1Left > nums2Right:
                right = i - 1
            else:
                left = i + 1
# @lc code=end

