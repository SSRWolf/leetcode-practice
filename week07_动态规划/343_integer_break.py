"""LeetCode 343. 整数拆分

题目条件：给定整数 n，将其拆分为至少两个正整数之和，并使这些整数的乘积最大。
返回最大乘积。
约束：2 <= n <= 58

示例 1：n = 2，返回 1
示例 2：n = 10，返回 36

先独立完成动态规划思路；此文件只提供题目说明和函数入口。
"""

#暴力解
class solution1:
    def integerBreak(self, n: int) -> int:
        maxmul = 0
        for i in range(1,n):     
            mul = i*(n-i)
            maxmul =  max(maxmul,mul)
            if n-i>1:
                mul = i * self.integerBreak(n-i)
                maxmul =  max(maxmul,mul)
        return maxmul

#贪心算法:每次分解优先拆出来一个3
class solution2:
    def integerBreak(self,n:int)->int:
        maxmul = 1
        if n<=3:
            return n-1
        while n>4:
            maxmul *= 3
            n=n-3
        return maxmul*n


#动态规划:继续拆分->j*(i-j)  不继续拆分：j*dp[i-j]
class solution3:
    def integerBreak(self, n: int) -> int:
        dp = [0] * (n + 1)
        maxmul=0
        for i in range(2, n + 1):
            for j in range(1, i):
                # 计算不继续拆分的乘积
                mul_notsplit = j*(i-j)

                # 计算继续拆分的乘积
                mul_split = j*dp[i-j]

                # 更新 dp[i]
                dp[i] = max(dp[i],mul_notsplit,mul_split)

        return dp[n]

#分治算法
class solution4:
    def best(self,x: int) -> int:
        # 1. 设计递归边界
        if x<4:
            return x
        # 2. 先考虑 x 不继续拆分
        best_mul = x
        # 3. 枚举左右两部分
        for i in range(1, x):
            left = self.best(i)
            right = self.best(x - i)
            # 4. 合并左右子问题
            best_mul = max(left*right,best_mul)
        return best_mul
        
    def integerBreak(self, n: int) -> int:
        max_mul = 0
        for i in range(1,n):
            left = self.best(i)
            right = self.best(n - i)
            max_mul = max(max_mul,left*right)
        
        return max_mul
    

if __name__ == "__main__":
    solution = solution4()

    test_cases = [
        (2, 1),
        (3, 2),
        (4, 4),
        (5, 6),
        (8, 18),
        (10, 36),
    ]

    for n, expected in test_cases:
        result = solution.integerBreak(n)
        print(
            f"输入 n={n}, 输出={result}, "
            f"预期={expected}, "
            f"{'通过' if result == expected else '失败'}"
        )
        
