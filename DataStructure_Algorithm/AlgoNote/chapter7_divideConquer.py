# 分治算法（Divide and Conquer）：即「分而治之」，把一个复杂问题拆分成多个相同或相似的子问题，
# 递归分解，直到子问题足够简单可以直接解决，最后将子问题的解合并得到原问题的解。

# 分治算法适用于满足以下 4 个条件的问题：
# 可分解：原问题能拆分为若干规模更小、结构相同的子问题。
# 子问题独立：各子问题互不影响，无重叠部分。
# 有终止条件：子问题足够小时可直接解决。
# 可合并：子问题的解能高效合并为原问题的解，且合并过程不能太复杂。

# 分治算法通用模板，伪代码
# def divide_and_conquer(problem_n):
#     """
#     分治算法通用模板
#     :param problem_n: 问题规模
#     :return: 原问题的解
#     """
#     # 1. 递归终止条件：当问题规模足够小时，直接解决
#     if problem_n < d:  # d 为可直接求解的最小规模
#         return solve(problem_n)  # 直接求解

#     # 2. 分解：将原问题分解为 k 个子问题
#     problems_k = divide(problem_n)  # divide 函数返回 k 个子问题的列表

#     # 3. 递归求解每个子问题
#     res = []
#     for sub_problem in problems_k:
#         sub_res = divide_and_conquer(sub_problem)  # 递归求解子问题
#         res.append(sub_res)  # 收集每个子问题的解

#     # 4. 合并：将 k 个子问题的解合并为原问题的解
#     ans = merge(res)
#     return ans  # 返回原问题的解

import numpy as np

class Solution:

    # 不小心写成了快排。。。
    # 但值得注意的是，快排的总体逻辑也采用了分治的思想
    def quickSort(self, nums:list[int])->list[int]:
        # 递归终止条件：数组长度=1
        if len(nums) == 1:
            return nums
        # 递归终止条件：数组中所有数都相等
        if all(nums[i]==nums[0] for i in range(len(nums))):
            return nums

        # 分解：将数组按大小分为数值小的一部分，和数值大的另一部分
        # 注意：1.没必要均匀分成一半，2.特殊情况：数组中有很多相同的数值
        k = np.random.randint(len(nums)) # 随机取“标杆数”，或称为哨兵，当然也可以选择头尾数
        belowK, aboveK = [], []
        for n in nums:
            if n <= nums[k]:
                belowK.append(n)
            else:
                aboveK.append(n)

        # 递归
        belowKSorted = self.quickSort(belowK)
        aboveKSorted = self.quickSort(aboveK)

        # 合并
        res = belowKSorted + aboveKSorted

        return res

    # 归并排序
    def mergeSort(self, nums:list[int])->list[int]:
        # 递归终止条件，数组长度为1
        if len(nums) == 1:
            return nums

        # 分解，取中间位置分成前后两段
        mid = len(nums) // 2
        frontPart = nums[:mid]
        backPart = nums[mid:]

        # 递归
        frontPartSort = self.mergeSort(frontPart)
        backPartSort = self.mergeSort(backPart)

        # 合并，其具体场景是合并2个有序数组，使用指针
        p, q, numsSort = 0, 0, []
        while p < len(frontPartSort) and q < len(backPartSort):
            if frontPartSort[p] <= backPartSort[q]:
                numsSort.append(frontPartSort[p])
                p += 1
            else:
                numsSort.append(backPartSort[q])
                q += 1
        if p == len(frontPartSort) and q < len(backPartSort):
            numsSort.extend(backPartSort[q:])
        elif p < len(frontPartSort) and q == len(backPartSort):
            numsSort.extend(frontPartSort[p:])

        return numsSort

    # 二分查找
    def HalfDivideSearch(self, nums:list[int], target:int)->int:
        # 左右指针
        left, right = 0, len(nums)-1
        mid = (left + right) // 2

        while left <= right:
            # 中间值小于目标值，往后继续找
            if nums[mid] < target:
                left = mid + 1
            # 中间值大于目标值，往前继续找
            elif nums[mid] > target:
                right = mid - 1
            else:
                return mid
            mid = (left + right) // 2

        return -1
            

s = Solution()

# 排序
# nums = list(map(int,input("请输入数组，空格隔开").split()))
# 快速排序
# numsSorted = s.quickSort(nums)
# print(numsSorted)
# 归并排序
# numsSorted = s.mergeSort(nums)
# print(numsSorted)

# 二分查找
nums = list(map(int, input("请输入升序数组，空格隔开").split()))
target = int(input("请输入目标值"))
k = s.HalfDivideSearch(nums, target)
print(k)