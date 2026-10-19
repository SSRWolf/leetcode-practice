"""Day 17 · LeetCode 83. 删除排序链表中的重复元素

初始条件：给定非递减链表 head，删除重复节点，使每个值只出现一次，返回头节点。
样例输入：head = [1,1,2,3,3]
样例结果：[1,2,3]

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

# LeetCode 运行环境提供 ListNode 节点类。
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        # 在这里写你的解法
        p = head
        while p and p.next:
            save = p
            while p.next and p.val == p.next.val :                
                p = p.next
            save.next = p.next
            p = p.next
        return head

#优化代码
class Solution2:
    def deleteDuplicates(self, head: ListNode | None) -> ListNode | None:
        p = head

        while p and p.next:
            if p.val == p.next.val:
                # 删除重复节点,跳过重复节点，但不移动 p，因为后面可能还有相同的值。
                p.next = p.next.next
                pass
            else:
                # 移动指针
                p = p.next
                pass

        return head