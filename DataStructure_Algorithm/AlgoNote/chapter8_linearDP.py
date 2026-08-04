
# 线性动态规划（线性 DP）：
# 指的是将问题的阶段按线性顺序划分，并基于此进行状态转移的动态规划方法。

# 即使状态有多个维度，只要每个维度的阶段划分都是线性的，也属于线性 DP。
# 例如，背包问题、区间 DP、数位 DP 等都属于线性 DP 的范畴。

# 线性 DP 问题的分类方式主要有两种：
# 按「状态维度」划分：可分为一维线性 DP、二维线性 DP 和多维线性 DP。
# 按「问题的输入格式」划分：可分为单串线性 DP、双串线性 DP、矩阵线性 DP 以及无串线性 DP。


# 单串线性 DP：
# 指输入为单个数组或字符串的线性动态规划问题。
# 阶段划分的方法是：以数组/字符串的结尾下标i或前i个元素作为阶段，对应 dp[i]
# 结尾下标i，前i个元素分别对应了序列和数组这2种情况
# 特殊地，对于第i个元素，有必须包含和可以不包含2种类型

# 单串线性 DP 问题中最经典的问题就是「最长递增子序列（Longest Increasing Subsequence，简称 LIS）」。

# 在某些单串线性 DP 问题中，单独用一个结束位置来定义状态无法完整刻画问题，
# 此时需要同时考虑两个结束位置，将状态定义为以这两个位置结尾，从而引入额外的维度。


# 双串线性 DP：
# 指输入为两个数组或两个字符串的线性动态规划问题。
# 常见的状态定义为 dp[i][j]，对应nums1[i]和nums2[j]构成的相关解

# 双串线性 DP 问题中最经典的问题就是「最长公共子序列（Longest Common Subsequence，简称 LCS）」
# 双串线性 DP 问题中除了经典的最长公共子序列问题之外，还包括字符串的模糊匹配问题。

# 最长重复子数组
def findLength(nums1: list[int], nums2: list[int]) -> int:
    len1 = len(nums1)
    len2 = len(nums2)

    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    dpMax = 0
    for i in range(len1):
        for j in range(len2):
            if nums1[i] == nums2[j]:
                dp[i+1][j+1] = dp[i][j] + 1
            dpMax = max(dpMax, dp[i+1][j+1])

    return dpMax

nums1 = [1,2,3,2,1]
nums2 = [3,2,1,4,7]
print(findLength(nums1, nums2))


# 矩阵线性 DP：
# 是指输入为二维矩阵的动态规划问题。
# 常见的状态定义为 dp[i][j]，表示从起点「(0,0)」到达「(i,j)」的最优解（如最小路径和、最大路径和等）。

# 最大正方形
def maximalSquare(matrix: list[list[str]]) -> int:
    len1, len2 = len(matrix), len(matrix[0])
    dp = [[0 for _ in range(len2+1)] for _ in range(len1+1)]
    dpMax = 0

    for i in range(len1):
        for j in range(len2):
            if matrix[i][j] == "1":
                dp[i+1][j+1] = min(dp[i][j], dp[i+1][j], dp[i][j+1]) + 1
            dpMax = max(dpMax, dp[i+1][j+1])

    return dpMax**2


# 无串线性 DP：
# 问题的输入不是显式的数组或字符串，但依然可分解为若干子问题的线性 DP 问题。

# 整数拆分
def integerBreak(n: int) -> int:
    dp = [1 for _ in range(n)]

    for i in range(1, n):
        for j in range(i):
            dp[i] = max(dp[i], max(dp[j],j+1)*(i-j))

    return dp[-1]

# def integerBreak(n: int) -> int:
#     pMax = 1
#     for k in range(2, n+1):
#         i = n // k
#         m = n.__mod__(k)
#         p = i ** (k-m) * (i+1) ** m
#         pMax = max(pMax, p)

#     return pMax

print(integerBreak(10))

# 只有两个键的键盘
def minSteps(n: int) -> int:
    dp = [float("inf")] * (n+1)
    dp[1] = 0
    for j in range(2, n+1):
        for i in range(1, j):
            if (j-i) % i == 0:
                print(i,j)
                dp[j] = min(dp[j], dp[i]+1+(j-i)//i)
    return dp[-1]

minSteps(8)

# 改进后代码
import math
class Solution:
    def minSteps(self, n: int) -> int:
        dp = [float("inf")] * (n+1)
        dp[0], dp[1] = 0, 0
        for i in range(2, n+1):
            for j in range(1, int(math.sqrt(i)) + 1):
                if i % j == 0:
                    dp[i] = min(dp[i], dp[j] + i // j, dp[i // j] + j)
        
        return dp[-1]