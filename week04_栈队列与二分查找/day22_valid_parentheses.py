"""Day 22 · LeetCode 20. 有效的括号

初始条件：给定只包含 ()[]{} 的字符串 s，判断括号是否正确闭合且顺序匹配。
样例输入：s = "()[]{}"
样例结果：True

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for i in range(len(s)):
            if s[i] in "([{": 
                stack.append(s[i])
            if  stack:
                if s[i] == ")" : 
                    if stack[-1] == "(":
                        stack.pop()
                    else:
                        return False
                if s[i] =="]":
                    if stack[-1] == "[":
                        stack.pop()
                    else:
                        return False
                if s[i] =="}":
                    if stack[-1] == "{":
                        stack.pop()
                    else:
                        return False
            else:
                return False
        if not stack:
            return True
        else:
            return False
