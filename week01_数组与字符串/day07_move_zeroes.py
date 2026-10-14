"""LeetCode 283. 移动零

题目初始条件：原地将 nums 中所有 0 移到末尾，并保持非零元素的相对顺序。函数不返回数组。
样例输入：nums = [0, 1, 0, 3, 12]
样例结果：nums 变为 [1, 3, 12, 0, 0]
请先独立完成；这里没有预填解法。
"""

#快慢指针
class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        # 在这里写你的解法
        fast = 0
        slow = 0
        for i in range(len(nums)):
            if nums[fast] != 0:
                nums[slow] = nums[fast]
                slow += 1
            fast += 1 
        for j in range(slow,(len(nums))):
            nums[j]=0
        
    
                
