"""Day 16 · LeetCode 21. 合并两个有序链表

初始条件：给定两个按非递减顺序排列的链表 list1 和 list2，合并后返回新链表头节点。
样例输入：list1 = [1,2,4]; list2 = [1,3,4]
样例结果：[1,1,2,3,4,4]

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

# LeetCode 运行环境提供 ListNode 节点类。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: ListNode | None, list2: ListNode | None) -> ListNode | None:
        # 在这里写你的解法
        dummy = ListNode(0)
        curr = dummy
        p1 = list1
        p2 = list2
        while  p1 and  p2 :
            if p1.val < p2.val:
                curr.next = p1
                p1=p1.next
                
            else:
                curr.next = p2
                p2 = p2.next
            curr = curr.next
        if p1:
            curr.next = p1
        else:
            curr.next = p2
            
        return dummy.next
