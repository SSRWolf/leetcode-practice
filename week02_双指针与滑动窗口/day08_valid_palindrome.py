"""LeetCode 125. 验证回文串

题目初始条件：只考虑字母和数字，忽略大小写，判断字符串 s 是否为回文串。
样例输入：s = "A man, a plan, a canal: Panama"
样例结果：True
请先独立完成；这里没有预填解法。
"""


class Solution:
    def isPalindrome(self, s: str) -> bool:
        # 在这里写你的解法
        behind = len(s)-1
        front = 0
        while behind > front:
            while not s[behind].isalnum() and behind>front:
                behind-=1
            while not s[front].isalnum() and behind>front:
                front += 1
            if s[front].lower() == s[behind].lower():
                behind-=1
                front += 1
            else:
                return False
        return True
