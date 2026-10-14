"""LeetCode 167. 两数之和 II

题目初始条件：给定非递减数组 numbers 和 target，找到两个数之和等于 target，返回从 1 开始的两个下标。
样例输入：numbers = [2, 7, 11, 15]; target = 9
样例结果：[1, 2]
请先独立完成；这里没有预填解法。
cd E:\postgraduate\leetCode

git add .
git commit -m "Complete Day 10"
git push
"""


class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        # 在这里写你的解法
        left  = 0
        right = len(numbers)-1
        while left<right:
            if numbers[left]+numbers[right]>target:
                right-=1
            elif numbers[left]+numbers[right]<target:
                left+=1
            else:
                return [left+1,right+1]
        return []