"""Day 20 · LeetCode 19. 删除链表的倒数第 N 个结点

初始条件：给定链表 head 和整数 n，删除倒数第 n 个节点并返回头节点。
样例输入：head = [1,2,3,4,5]; n = 2
样例结果：[1,2,3,5]

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

# LeetCode 运行环境提供 ListNode 节点类。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

#思路是fast比slow多走n步，fast到末尾时slow到倒数第n个节点的前一个节点
#注意slow指向要删除节点的前一个节点，因此如果要删除的是头结点，需要一个虚拟节点在头结点之前
class Solution:
    def removeNthFromEnd(self, head: ListNode | None, n: int) -> ListNode | None:        
        dummy = ListNode(0)
        dummy.next = head
        slow = dummy
        fast = dummy
        while n+1>0 and fast:
            fast = fast.next
            n-=1
        while fast:
            slow = slow.next
            fast = fast.next
        if slow:
            delete = slow.next
            slow.next = delete.next
        
        return dummy.next
