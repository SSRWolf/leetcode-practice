"""LeetCode 11. 盛最多水的容器

题目初始条件：给定高度数组 height，选择两条竖线和 x 轴组成容器，返回可盛水的最大面积。
样例输入：height = [1, 8, 6, 2, 5, 4, 8, 3, 7]
样例结果：49
请先独立完成；这里没有预填解法。
"""


class Solution:
    def maxArea(self, height: list[int]) -> int:
        # 在这里写你的解法
        left = 0
        right = len(height)-1
        maxv = 0
        while right>left:
            v = min(height[left],height[right])*(right-left)
            maxv = max(maxv,v)
            if height[right]>height[left]:
                left+=1
            else:
                right-=1
        return maxv
