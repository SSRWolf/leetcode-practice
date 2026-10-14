"""LeetCode 977. 有序数组的平方

题目初始条件：给定按非递减顺序排列的 nums，返回各元素平方后仍按非递减顺序排列的新数组。
样例输入：nums = [-4, -1, 0, 3, 10]
样例结果：[0, 1, 9, 16, 100]
请先独立完成；这里没有预填解法。
"""


class Solution:
    #新建数组后排序
    def sortedSquares(self, nums: list[int]) -> list[int]:
        # 在这里写你的解法
        ans=[]
        for i in range(len(nums)):
            ans.append(nums[i]*nums[i])
        ans.sort()
        return ans

    #双指针
    def sortedSquares2(self, nums: list[int]) -> list[int]:
        ans=[0]*len(nums)
        front = 0
        behind = len(nums)-1
        i = len(nums)-1
        while behind>=front:
            if nums[front]**2>nums[behind]**2:
                ans[i]=nums[front]**2
                front += 1
            else:
                ans[i]=nums[behind]**2
                behind -= 1
            i-=1
            

        return ans

