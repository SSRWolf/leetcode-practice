"""LeetCode 14. 最长公共前缀

题目初始条件：给定字符串数组 strs，返回所有字符串的最长公共前缀；没有则返回空字符串。
样例输入：strs = ["flower", "flow", "flight"]
样例结果："fl"
请先独立完成；这里没有预填解法。
"""

#纵向扫描
class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:

        s = strs[0]

        for i in range(len(s)):

            for j in range(1, len(strs)):

                # 判断是否超出字符串长度
                if i>=len(strs[j]):
                    return s[:i]

                # 判断两个字符是否相同
                if strs[j][i] != s[i]:
                    return s[i]

                # 如果不能继续匹配，返回目前的公共前缀
        return s

#横向扫描    

    def longestCommonPrefix2(self, strs: list[str]) -> str:

        prefix = strs[0]

        for i in range(1, len(strs)):

            # 1. 判断 strs[i] 是否以 prefix 开头
            while not strs[i].startswith(prefix):

            # 2. 如果不是，就缩短 prefix
                prefix = prefix[:-1]
            # 3. 如果 prefix 已经变成空字符串
            if prefix == "":
            #    可以直接返回
                return prefix

        return prefix

       