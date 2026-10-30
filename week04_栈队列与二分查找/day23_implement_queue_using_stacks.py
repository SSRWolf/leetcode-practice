"""Day 23 · LeetCode 232. 用栈实现队列

初始条件：仅用两个栈实现先进先出队列；实现 push、pop、peek、empty。
样例输入：push(1), push(2), peek(), pop(), empty()
样例结果：1, 1, False

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

class MyQueue:
    def __init__(self):
        # 初始化队列    
        self.stack_in = []
        self.stack_out = []
        pass

    def push(self, x: int) -> None:
        self.stack_in.append(x)
        pass

    def pop(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                x = self.stack_in[-1]
                self.stack_out.append(x)
                self.stack_in.pop()
        if self.stack_out:
            y = self.stack_out[-1]
            self.stack_out.pop()
        return y


    def peek(self) -> int:
        if not self.stack_out:
            while self.stack_in:
                self.stack_out.append(self.stack_in.pop())

        return self.stack_out[-1]

    def empty(self) -> bool:
        if not self.stack_in and not self.stack_out:
            return True
        return False
q = MyQueue()
q.push(1)
q.push(2)

print(q.peek())   # 1
print(q.pop())    # 1
print(q.peek())   # 2
print(q.empty())  # False
print(q.pop())    # 2
print(q.empty())  # True