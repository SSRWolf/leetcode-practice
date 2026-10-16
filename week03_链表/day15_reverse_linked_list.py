"""Day 15 · LeetCode 206. 反转链表

初始条件：给定单链表头节点 head，反转链表并返回新的头节点。
样例输入：head = [1,2,3,4,5]
样例结果：[5,4,3,2,1]

请先独立写解法。下面仅给出题目入口，不包含答案。
"""

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # 在这里写你的代码
        pre = None
        curr = head
        save = None
        while curr:
            save = curr.next        
            curr.next = pre         
            pre = curr
            curr = save
        return pre
