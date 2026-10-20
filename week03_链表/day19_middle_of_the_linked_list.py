"""Day 19 · LeetCode 876. 链表的中间结点

初始条件：给定链表头节点 head，返回中间节点；若有两个中间节点，返回第二个。
样例输入：head = [1,2,3,4,5,6]
样例结果：值为 4 的节点

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

# LeetCode 运行环境提供 ListNode 节点类。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#先找链表长度
class Solution:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        p = head
        length = 0
        count = 0
        while p:
            length += 1
            p = p.next
        p = head
        while count<(length//2) and p:
            count += 1
            p = p.next
        return p

#快慢指针：快走两步，慢走一步，当快指针走到结尾，慢指针刚好在中间
class Solution2:
    def middleNode(self, head: ListNode | None) -> ListNode | None:
        fast = head
        slow = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next

        return slow


    