"""LeetCode 26. 删除有序数组中的重复项

题目初始条件：原地移除非递减数组 nums 中的重复元素，让每个不同元素只出现一次；返回不同元素个数 k，前 k 项应为去重结果。
样例输入：nums = [1, 1, 2]
样例结果：返回 2，nums 的前两项为 [1, 2]
请先独立完成；这里没有预填解法。
"""


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        # 在这里写你的解法
        fast = 1
        slow = 0
        while fast<len(nums):
            while  fast<len(nums) and nums[fast] == nums[slow] :
                fast+=1         
            if fast<len(nums):
                slow+=1
                nums[slow]=nums[fast]
                fast+=1
        return slow+1
