"""Day 28 · LeetCode 153. 寻找旋转排序数组中的最小值

题目条件：nums 原本是升序数组，所有元素互不相同，经过若干次旋转后，
返回其中的最小元素。数组也可能旋转后仍保持升序。
要求：设计时间复杂度为 O(log n) 的算法。
约束：1 <= len(nums) <= 5000；-5000 <= nums[i] <= 5000。

示例 1：nums = [3, 4, 5, 1, 2]，返回 1。
示例 2：nums = [4, 5, 6, 7, 0, 1, 2]，返回 0。
示例 3：nums = [11, 13, 15, 17]，返回 11。

请先独立完成。下面仅提供函数入口，不包含解法。
"""

from __future__ import annotations


class Solution:
    def findMin(self, nums: list[int]) -> int:
        low = 0
        high = len(nums)-1
        while high>low:
            mid = (high+low)//2
            #最小值在右侧
            if nums[high]<nums[mid]:
                    low = mid+1
            #最小值在左侧
            else:
                    high = mid
        return nums[low]
