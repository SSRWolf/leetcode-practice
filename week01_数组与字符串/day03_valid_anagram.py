"""
LeetCode 242 - 有效的字母异位词
"""

# 方法一：双字典分别计数，再比较（你提交并修正过的思路）
class SolutionTwoDicts:
    def isAnagram(self, s: str, t: str) -> bool:
        d1 = {}
        d2 = {}
        for i in s:
            if i in d1:
                d1[i] += 1
            else:
                d1[i] = 1
        for j in t:
            if j in d2:
                d2[j] += 1
            else:
                d2[j] = 1
        return d1 == d2


# 方法二：单字典，先加后减，最后检查是否全部为 0（你提交的版本）
class SolutionOneDict:
    def isAnagram(self, s: str, t: str) -> bool:
        d = {}
        if len(s) != len(t):
            return False
        for i in s:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1
        for j in t:
            if j in d:
                d[j] -= 1
            else:
                return False
        for i in d:
            if d[i] != 0:
                return False
        return True


# 提交到 LeetCode 时，选择一种方法，将类名改为 Solution。
