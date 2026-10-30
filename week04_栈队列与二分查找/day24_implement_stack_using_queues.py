"""Day 24 · LeetCode 225. 用队列实现栈

初始条件：仅用队列实现后进先出栈；实现 push、pop、top、empty。
样例输入：push(1), push(2), top(), pop(), empty()
样例结果：2, 2, False

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations
from collections import deque

#双队列实现：出队到其中一个队列只剩下一个元素就是栈顶元素
class MyStack:
    def __init__(self):
        # 初始化队列
        self.queue1 = deque()
        self.queue2 = deque()
        pass

    def push(self, x: int) -> None:
        self.queue1.append(x)
        pass

    def pop(self) -> int:
        while len(self.queue1)>1:
            x = self.queue1.popleft()
            self.queue2.append(x)
        y = self.queue1.popleft()
        self.queue1, self.queue2 = self.queue2, self.queue1
        return y

    def top(self) -> int:
        while len(self.queue1)>1:
            x = self.queue1.popleft()
            self.queue2.append(x)
        topnum = self.queue1.popleft()
        self.queue2.append(topnum)
        self.queue1, self.queue2 = self.queue2, self.queue1
        return topnum

    def empty(self) -> bool:
        if not self.queue1 and not self.queue2:
            return True
        else:
            return False

#单队列实现：
class MyStack2:
    def __init__(self):
        # 初始化队列
        self.queue = deque()
        pass

    def push(self, x: int) -> None:
        self.queue.append(x)
        qlen = len(self.queue)
        for i in range(1,qlen):
            x = self.queue.popleft()
            self.queue.append(x)
        pass

    def pop(self) -> int:
       return self.queue.popleft()
    
    def top(self) -> int:
        return self.queue[0]

    def empty(self) -> bool:
        if not self.queue:
            return True
        else:
            return False
