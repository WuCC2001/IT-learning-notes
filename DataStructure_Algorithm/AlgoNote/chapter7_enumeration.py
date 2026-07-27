# 确定枚举对象、枚举范围、约束条件

# 它适用于规模较小、可快速验证答案的问题，或作为基线方案、结果校验与对拍工具。
# 实战中应尽量结合剪枝（添加约束、提前判定不可能）、缩小搜索空间（利用对称性、边界与不变量）、
# 降维与变量替换、以及避免重复计算等手段，显著提升效率。

# 实践建议是：先写出「能过的暴力正确解」，再围绕「减分支、减范围、减重算」迭代优化；
# 当复杂度仍难以接受时，考虑切换到更合适的范式，例如哈希加速、双指针与滑动窗口、二分查找、分治、动态规划或图算法等。

import math

class Solution():

    # 问题：百钱买百鸡问题
    # 公鸡 5 元/只，母鸡 3 元/只，小鸡 1 元/3 只。用 100 元买 100 只鸡，问各买多少只？
    def buyChicken(self):
        for x in range(0, 21):
            for y in range(0, 34):
                # for z in range(0, 100):
                #     if x + y + z == 100 and 5 * x + 3 * y + z / 3 == 100:
                #         print(x, y, z)
                if 5 * x + 3 * y + (100-x-y)/3 == 100:
                    print(x, y, 100-x-y)

    # 问题：两数之和
    def twoSum(self, nums: list, target: int):
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i] + nums[j] == target:
                    return [i, j]
            return []

    def twoSumHash(self, nums: list, target: int):
        hashmap = {}
        for i in range(len(nums)):
            hashmap[nums[i]] = i
        for i in range(len(nums)):
            complement = target - nums[i]
            if complement in hashmap and hashmap[complement] != i:
                return [i, hashmap[complement]]
        return []

    # 问题：统计平方和三元组的数目
    def tribleSquareSum(self, n: int)->int:
        cnt = 0
        for c in range(1, n+1):
            for b in range(1, c):
                # for a in range(1, c):
                #     if a**2 + b**2 == c**2:
                a = int(math.sqrt(c**2-b**2))
                if a**2 + b**2 == c**2:
                        cnt += 1
                        print(a,b,c)
        return cnt

s = Solution()

# 问题：百钱买百鸡问题
# s.buyChicken()

# 问题：两数之和
# nums = list(map(int, input("请输入数组元素，以空格分隔: ").split()))
# target = int(input("请输入目标值: "))
# print(s.twoSum(nums, target))
# print(s.twoSumHash(nums, target))

# 问题：统计平方和三元组的数目
n = int(input("请输入目标值: "))
cnt = s.tribleSquareSum(n)
print(cnt)
