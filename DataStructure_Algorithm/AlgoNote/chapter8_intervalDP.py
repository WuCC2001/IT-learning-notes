
# 区间动态规划（区间 DP）：
# 是一类以区间为阶段、以区间的左右端点为状态的动态规划方法。
# 它常用于解决「在一段区间内进行某种操作，使得总代价最小或总价值最大」这类问题。

# 区间 DP 的核心思想是：先解决小区间的最优解，再逐步合并得到大区间的最优解，最终得到整个区间的最优解。
# 区间 DP 的状态通常用 dp[i][j] 表示区间 [i,j] 的最优解。状态的转移依赖于比 [i,j] 更小的子区间的状态。

# 常见的区间 DP 问题大致分为两类：
# 单区间扩展型：
#   通过在区间 [i+1,j-1] 的基础上，向两侧扩展得到 [i,j] 例如回文串、石子合并等问题。
# 多区间合并型：
#   将区间 [i,j] 拆分为两个或多个更小的区间(如 [i,k] 和 [k+1,j])，通过合并这些小区间的最优解得到大区间的最优解。‘


# 单区间扩展型解题思路

# 这类区间 DP 通常是「从中间向两侧扩展」，基本解题流程如下：
# 枚举区间起点 i ；
# 枚举区间终点 j ；
# 按照状态转移方程，利用更小区间的最优解递推出更大区间的最优解。

# dp[i][j]代表区间 [i,j] 上的最优解
# cost[i][j]表示将小区间扩展到大区间产生的代价

# for i in range(size - 1, -1, -1):       # 枚举区间起点
#     for j in range(i + 1, size):        # 枚举区间终点
#         # 状态转移方程
#         dp[i][j] = f(dp[i + 1][j - 1], dp[i + 1][j], dp[i][j - 1]) + cost[i][j]

# 多区间合并型解题思路

# 这类区间 DP 的核心思想是：将大区间拆分成小区间，通过合并子区间的最优解，得到大区间的最优解。

# 这类区间 DP 的通用解题步骤如下：
# 枚举区间长度（从小到大，保证子区间已被计算）；
# 枚举区间起点 i ，根据区间长度确定终点 j ；
# 枚举所有可能的分割点 k ，用状态转移方程更新 dp[i][j] 的最优值。

# for l in range(1, n):               # 枚举区间长度
#     for i in range(n):              # 枚举区间起点
#         j = i + l - 1               # 根据起点和长度得到终点
#         if j >= n:
#             break
#         dp[i][j] = float('-inf')    # 初始化 dp[i][j]
#         for k in range(i, j + 1):   # 枚举区间分割点
#             # 状态转移方程，计算合并区间后的最优值
#             dp[i][j] = f(dp[i][j], dp[i][k] + dp[k + 1][j] + cost[i][j])


# 区间 DP 问题的应用

# 最长回文子序列
class Solution:
    def longestPalindromeSubseq(self, s: int) -> int:
        size = len(s)
        dp = [[0 for _ in range(size)] for _ in range(size)]
        for i in range(size):
            dp[i][i] = 1

        for i in range(size - 1, -1, -1):
            for j in range(i + 1, size):
                if s[i] == s[j]:
                    dp[i][j] = dp[i + 1][j - 1] + 2
                else:
                    dp[i][j] = max(dp[i + 1][j], dp[i][j - 1])

        return dp[0][size - 1]

# 戳气球
# 核心在于定义状态和状态转移方程
# 定义状态：dp[i][j]表示戳破气球 i 与 j 之间所有气球（不包含气球 i 和 j ），所能获取的最多硬币数。
# 状态转移方程：假设气球 i 与 j 之间，“最后一个被戳破”的气球编号为 k
# 这样就能得到方程为：dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
class Solution:
    def maxCoins(self, nums: list[int]) -> int:
        # 两端添加1，表示边界情况
        nums.insert(0, 1)
        nums.insert(len(nums), 1)
        size = len(nums)
        # dp[i][j]表示戳破气球 i 与 j 之间所有气球（不包含气球 i 和 j ），所能获取的最多硬币数。
        dp = [[0 for _ in range(size)] for _ in range(size)]

        for i in range(size-2, -1, -1):
            for j in range(i+1, size):
                # 假设气球 i 与 j 之间，“最后一个被戳破”的气球编号为 k
                for k in range(i+1, j):
                    dp[i][j] = max(dp[i][j], dp[i][k]+dp[k][j]+nums[i]*nums[k]*nums[j])
        
        return dp[0][-1]