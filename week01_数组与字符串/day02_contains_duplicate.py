"""
LeetCode 217 - 存在重复元素
"""

# 方法一：集合去重后比较长度（你独立提交并通过的版本）
class SolutionByLength:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for i in nums:
            s.add(i)
        if len(s) < len(nums):
            return True
        else:
            return False


# 方法二：遍历时判断，发现重复立即返回（你提交的版本，统一缩进）
class SolutionEarlyReturn:
    def containsDuplicate(self, nums: list[int]) -> bool:
        s = set()
        for i in nums:
            if i in s:
                return True
            else:
                s.add(i)
        return False


# 提交到 LeetCode 时，选择一种方法，将类名改为 Solution。
