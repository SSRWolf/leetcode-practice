"""Day 21 · LeetCode 2. 两数相加

初始条件：两个链表以逆序存储非负整数的各位数字，返回和的逆序链表。
样例输入：l1 = [2,4,3]; l2 = [5,6,4]
样例结果：[7,0,8]

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

from __future__ import annotations

# LeetCode 运行环境提供 ListNode 节点类。
class ListNode:
    def __init__(self,val=0,next=None):
        self.val = val
        self.next = next

#结果不需要翻转 因为给的就是已经反转的链表
class Solution:
    def addTwoNumbers(self, l1: ListNode | None, l2: ListNode | None) -> ListNode | None:
        p1 = l1
        p2 = l2
        p = ListNode(0)
        dummy = p
        carry = 0
        total = 0
        #total要注意边界：如果p1在且p2不在 p1为0；p2在且p1不在 p1为0；如果两个都不在要记得保留进位
        while p1 or p2 or carry != 0:
            if p1 and p2:
                total = p1.val + p2.val + carry
            elif not p1 and p2:
                total = p2.val + carry
            elif not p2 and p1:
                total = p1.val + carry
            else:
                total = carry
            #carry, unit = divmod(total, 10) divmod 可以同时返回%和//
            carry = total//10
            unit = total%10
            pn = ListNode(unit)
            p.next = pn
            p = p.next
            #因为两个链表长度可能不一样，这里也需要判断p1,p2是否已经为空
            if p1:
                p1 = p1.next
            if p2:    
                p2 = p2.next
        return dummy.next
