"""LeetCode 3. 无重复字符的最长子串

题目初始条件：给定字符串 s，返回不含重复字符的最长连续子串的长度。
样例输入：s = "abcabcbb"
样例结果：3
请先独立完成；这里没有预填解法。
"""


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # 在这里写你的解法
        seen = set()
        left = 0
        right = 0
        maxlen = 0
        while right<len(s):
            while s[right] in seen:
                seen.remove(s[left])
                left+=1     
            if not s[right] in seen:
                seen.add(s[right]) 
            maxlen = max(maxlen,right-left+1)
            right+=1
        return maxlen
        
