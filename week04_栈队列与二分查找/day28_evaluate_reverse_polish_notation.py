"""Day 28 · LeetCode 150. 逆波兰表达式求值

初始条件：给定逆波兰表达式的字符串数组 tokens，计算整数结果；除法向零截断。
样例输入：tokens = ["2","1","+","3","*"]
样例结果：9

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

class Solution:
    def evalRPN(self, tokens: list[str]) -> int:
        i=0
        stack = []
        ans = 0
        while i<len(tokens):
            if not tokens[i] in ["+","-","*","/"]: 
                stack.append(int(tokens[i]))
            else:
                if tokens[i]=="+":
                    right = stack.pop()
                    left = stack.pop()
                    ans = left+right
                    stack.append(ans)
                elif tokens[i] == "-":
                    right = stack.pop()
                    left = stack.pop()
                    ans = left-right
                    stack.append(ans)
                elif tokens[i] == "*": 
                    right = stack.pop()
                    left = stack.pop()
                    ans = left*right 
                    stack.append(ans) 
                elif tokens[i] == "/": 
                    right = stack.pop()
                    left = stack.pop() 
                    ans = abs(left)//abs(right)
                    if (left<0) != (right<0):
                        stack.append(-ans)   
                    else:
                        stack.append(ans)
            i+=1
        return stack[-1]