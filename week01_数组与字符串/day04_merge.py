#LeetCode 88. 合并两个有序数组


class Solution:
    def merge(
        self,
        nums1: list[int],
        m: int,
        nums2: list[int],
        n: int
    ) -> None:

        # 三个指针，分别指向两个数组的末尾
        # 以及 nums1 最后一个可填充的位置
        i = m - 1  #指向nums1
        j = n - 1  #指向nums2
        k = m + n - 1

        # 请在这里编写你的代码
        while (i>=0 and j>=0):
            if nums2[j]>nums1[i]:
                nums1[k]=nums2[j]
                j-=1
            else:
                nums1[k]=nums1[i]              
                i-=1
            
            k-=1
        while j>=0:
            nums1[k]=nums2[j]
            j-=1
            k-=1

       