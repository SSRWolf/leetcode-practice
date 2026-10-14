"""LeetCode 209. 长度最小的子数组

题目初始条件：给定正整数数组 nums 和正整数 target，返回元素和至少为 target 的连续子数组的最短长度；不存在则返回 0。
样例输入：target = 7; nums = [2, 3, 1, 2, 4, 3]
样例结果：2
请先独立完成；这里没有预填解法。
"""


class Solution:
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        # 在这里写你的解法
        left=0
        window_sum=0
        minlen = float("inf")
        for right in range(len(nums)):
            window_sum+=nums[right]
            while window_sum>=target:
                numslen = right-left+1
                minlen=min(minlen,numslen)
                window_sum-=nums[left] 
                left+=1
                             
        if minlen == float("inf"):
            return 0
        else:
            return int(minlen)
