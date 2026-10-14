#LeetCode 1 - 两数求和

class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:

        d = {}

        for i in range(len(nums)):

            a = target - nums[i]

            # 1. 判断 a 是否已经在字典中
            # 2. 如果存在，返回对应的两个下标
            if a in d:
                j = d[a]
                return [i,j]
            # 3. 否则记录当前元素和下标
            else:
                d[nums[i]]=i
