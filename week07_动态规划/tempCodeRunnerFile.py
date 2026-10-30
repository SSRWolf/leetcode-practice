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
    