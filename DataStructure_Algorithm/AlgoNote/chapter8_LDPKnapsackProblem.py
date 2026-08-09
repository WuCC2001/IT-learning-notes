
# 背包问题：
# 背包问题是线性 DP 问题中一类经典模型。其基本描述为：给定若干物品，每种物品有各自的重量、价值和数量限制，
# 以及一个最大承重为 W 的背包。要求在不超过背包承重上限的前提下，选择若干物品放入背包，
# 使得背包内物品的总价值最大。

# 根据物品数量和选择方式的不同，背包问题主要分为：
# 0-1 背包问题、完全背包问题、多重背包问题、分组背包问题和混合背包问题等类型。


# 0-1 背包问题
# 给定 n 件物品和一个最大承重为 W 的背包。每件物品的重量为 weight[i]，价值为 value[i]，每种物品只能选择一次。
# 请问在不超过背包承重的前提下，最多能获得多少总价值？

# 0-1 背包问题的核心：每种物品只能选一次，可以选择放或不放。

# 1. 阶段划分、
#   以物品序号和当前背包容量为阶段。
# 2. 定义状态
#   dp[i][w]：前 i 件物品，放入容量不超过 w 的背包时可获得的最大价值。
# 3. 状态转移方程
#   只需关注第 i 件物品（对应起始下标1）的选择情况（即放或不放）
#   代码给出的 i-1 对应起始下标0
    # if w < weight[i - 1]:
    #     # 当前物品放不下，继承上一个状态
    #     dp[i][w] = dp[i - 1][w]
    # else:
    #     # 当前物品能放下，取放与不放的最大值
    #     dp[i][w] = max(
    #         dp[i - 1][w],  # 不放当前物品
    #         dp[i - 1][w - weight[i - 1]] + value[i - 1]  # 放当前物品
    #     )
# 4. 初始条件
#   dp[i][0] = 0, dp[0][w] = 0
# 5. 最终结果
#   dp[size][W]


# 滚动数组优化
# 通过前面的分析可以发现，在依次处理第 1∼n 件物品时，
# 「前 i 件物品的状态」只依赖于「前 i−1 件物品的状态」，与更早之前的状态无关。
# 换句话说，状态转移时只涉及当前行（第i行）的dp[i][w]和上一行（第i−1行）的dp[i−1][w]、dp[i−1][w−weight[i−1]]。
# 因此，我们无需保存所有阶段的状态，只需保留当前阶段和上一阶段的状态即可。
# 可以用两个一维数组分别存储相邻两阶段的所有状态：dp[0][w] 存储 dp[i−1][w]，dp[1][w] 存储 dp[i][w]。

# 进一步优化时，其实只需一个一维数组 dp[w]，利用「滚动数组」思想，将动态规划的第一维去掉，从而实现空间优化。

# 在处理第 i 件物品时，dp[w] 只依赖于上一阶段（即第 i−1 件物品处理完后）的 dp[w] 和 dp[w−weight[i−1]]。
# 因此，为了避免状态被提前覆盖，必须对 w 采用从大到小（即从 W 到 0）的逆序遍历。
# 这样可以确保每次转移用到的 dp[w−weight[i−1]] 仍然是上一阶段的值。
# 如果采用从小到大（正序）遍历，则 dp[w−weight[i−1]] 可能已经被本轮更新，导致状态转移错误。

# 实际上，当 w<weight[i−1] 时，当前物品无法放入背包，dp[w] 保持不变，无需更新。
# 因此逆序遍历时只需从 W 遍历到 weight[i−1]。

# 滚动数组优化后代码
# 1. 阶段划分、
#   以当前背包容量为阶段。
# 2. 定义状态
#   dp[w]：容量不超过 w 的背包时可获得的最大价值。
# 3. 状态转移方程
#   只需关注第 i 件物品的选择情况（即放或不放）
    # # 遍历每一件物品
    # for i in range(size):
    #     # 必须逆序遍历容量，防止状态被提前覆盖
    #     for w in range(W, weight[i] - 1, -1):
    #         dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
# 4. 初始条件
#   dp[w] = 0
# 5. 最终结果
#   dp[W]
class Solution:
    # 思路 2：动态规划 + 滚动数组优化
    def zeroOnePackMethod2(self, weight: list[int], value: list[int], W: int) -> int:
        """
        0-1 背包问题的滚动数组优化解法
        :param weight: List[int]，每件物品的重量
        :param value: List[int]，每件物品的价值
        :param W: int，背包最大承重
        :return: int，背包可获得的最大价值
        """
        size = len(weight)
        # dp[w] 表示容量为 w 时背包可获得的最大价值
        dp = [0] * (W + 1)

        # 遍历每一件物品
        for i in range(size):
            # 必须逆序遍历容量，防止状态被提前覆盖
            for w in range(W, weight[i] - 1, -1):
                # 状态转移：不选第 i 件物品 or 选第 i 件物品
                # dp[w] = max(不选, 选)
                dp[w] = max(dp[w], dp[w - weight[i]] + value[i])
                # 解释：
                # dp[w]：不选第 i 件物品，价值不变
                # dp[w - weight[i]] + value[i]：选第 i 件物品，容量减少，相应加上价值

        return dp[W]

# 0-1 背包问题的应用
# 经典题目包括：分割等和子集，目标和

# 分割等和子集
# 本题实质是：能否从数组中选出若干元素，使其和恰好等于整个数组元素和的一半（记为target）。
# 问题转化为：给定物品数组，每件物品的重量和价值相等，每件物品最多选一次，问能否恰好装满容量为target的背包？
# 恰好装满容量为target的背包，等价于：容量为target的背包，最大价值是否能达到target？

# 最后一块石头的重量 II
# 问题等价于：在元素前填充加号和减号，得到最小结果（大于等于0）
# 结合数组的总和sum，可以等价变化为：选取一定的元素，得到最大的和（小于等于sum/2）

def lastStoneWeightII(stones: list[int]) -> int:
    halfSum = sum(stones) // 2
    dp = [0] * (halfSum + 1)

    # dp[w]的含义是：容量为w的背包最多能装下的重量
    for i in range(len(stones)):
        for w in range(halfSum, stones[i] - 1, -1):
            dp[w] = max(dp[w], dp[w - stones[i]] + stones[i])

    return sum(stones) - 2 * dp[-1]

stones = [31,26,33,21,40]
print(lastStoneWeightII(stones))


# 完全背包问题
# 给定 n 件物品和一个最大承重为 W 的背包。每件物品的重量为 weight[i]，价值为 value[i]，且每种物品的数量不限。
# 请问在不超过背包承重的前提下，最多能获得多少总价值？

# 完全背包问题的核心特性：每种物品可以选取任意多次（数量无限）。

# 完全背包问题与 0-1 背包问题的状态定义和基本思路类似，不同之处在于每种物品可以被多次选择。
# 因此，可以在动态规划的基础上增加一层循环，枚举第i-1种物品的选取数量
# 从而将完全背包问题转化为多重选择的 0-1 背包问题模型。

# 状态dp[i][w]是一个二维数组，其中第一维代表「当前正在考虑的物品种类」，第二维表示「当前背包的载重上限」，
class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def completePackMethod1(self, weight: list[int], value: list[int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(w // weight[i - 1] + 1):
                    # dp[i][w] 取所有 dp[i - 1][w - k * weight[i - 1] + k * value[i - 1] 中最大值
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - k * weight[i - 1]] + k * value[i - 1])
        
        return dp[size][W]

# 状态转移方程优化
# dp[i][w]展开有k+1项，dp[i-1][w]展开有k项
# 且dp[i][w]展开的第2到k+1项，和dp[i-1][w]展开的第1到k项对应，前者每项多了个value[i - 1]
class Solution:
    # 思路 2：动态规划 + 状态转移方程优化
    def completePackMethod1(self, weight: list[int], value: list[int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 第 i - 1 件物品装不下
                if w < weight[i - 1]:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」
                    dp[i][w] = dp[i - 1][w]
                else:
                    # dp[i][w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                    dp[i][w] = max(dp[i - 1][w], dp[i][w - weight[i - 1]] + value[i - 1])
                    
        return dp[size][W]

# 可以看到，这个状态转移方程与 0-1 背包问题的状态转移方程非常相似。
# 唯一的区别在于：
# 0-1 背包问题中，转移用的是dp[i - 1][w - weight[i - 1]]，即上一阶段的状态；
# 完全背包问题中，转移用的是dp[i][w - weight[i - 1]，即当前阶段的状态。
# 因此 0-1 背包问题的滚动优化是逆序，而完全背包问题的滚动优化是正序

# 滚动数组优化
class Solution:
    # 思路 3：动态规划 + 滚动数组优化
    def completePackMethod1(self, weight: list[int], value: list[int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 正序枚举背包装载重量
            for w in range(weight[i - 1], W + 1):
                # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
                
        return dp[W]
# 组合总和 IV
# 个人认为不属于背包问题（严格意义），因为是求组合数（不对应实际意义），而非计算总价值
class Solution:
    def combinationSum4(self, nums: list[int], target: int) -> int:
        size = len(nums)
        # dp[w]表示总和为w的组合个数
        dp = [0 for _ in range(target + 1)]
        dp[0] = 1
        
        for w in range(1, target + 1):
            for i in range(size):
                if nums[i] <= w:
                    dp[w] += dp[w - nums[i]]
                
        return dp[-1]


# 多重背包问题
# 有 n 种物品和一个最多能装重量为 W 的背包，第 i 种物品的重量为 weight[i]，价值为 value[i]，件数为 count[i]。
# 请问在总重量不超过背包载重上限的情况下，能装入背包的最大价值是多少？

# 核心思路：将「完全背包问题」类比「0-1 背包问题」进行处理

class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def multiplePackMethod1(self, weight: list[int], value: list[int], count: list[int], W: int):
        size = len(weight)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(min(count[i - 1], w // weight[i - 1]) + 1):
                    # dp[i][w] 取所有 dp[i - 1][w - k * weight[i - 1] + k * value[i - 1] 中最大值
                    dp[i][w] = max(dp[i][w], dp[i - 1][w - k * weight[i - 1]] + k * value[i - 1])
                    
        return dp[size][W]

# 滚动数组优化

# 在完全背包问题中，我们通过优化状态转移方程的方式，成功去除了对物品件数k的依赖，从而将时间复杂度下降了一个维度。
# 而在多重背包问题中，我们在递推dp[i][w]时，是无法从 dp[i][w-weight[i-1]] 状态得知目前究竟已经使用了多少件第i-1种物品，
# 也就无法判断第i-1种物品是否还有剩余数量可选。这就导致了我们无法通过优化状态转移方程的方式将多重背包问题的时间复杂度降低。

# 但是我们可以参考「完全背包问题」+「滚动数组优化」的方式，将算法的空间复杂度下降一个维度。
class Solution: 
    # 思路 2：动态规划 + 滚动数组优化
    def multiplePackMethod1(self, weight: list[int], value: list[int], count: list[int], W: int):
        size = len(weight)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight[i - 1] - 1, -1):
                # 枚举第 i - 1 种物品能取个数
                for k in range(min(count[i - 1], w // weight[i - 1]) + 1):
                    # dp[w] 取所有 dp[w - k * weight[i - 1]] + k * value[i - 1] 中最大值
                    dp[w] = max(dp[w], dp[w - k * weight[i - 1]] + k * value[i - 1])
                
        return dp[W]

# 二进制优化
# 虽然无法通过优化「状态转移方程」的方式将「多重背包问题」的时间复杂度降低。
# 但我们还是可以从物品数量入手，通过「二进制优化」的方式，将算法的时间复杂度降低。

# 二进制优化的具体操作：
# 简单来说，就是把物品的数量 count[i] 拆分成「由 1, 2, 4, …, 2^m 件单个物品组成的大物品」，
# 以及「剩余不足 2 的整数次幂数量的物品组成的大物品」。
# 这些大物品通过不同的组合，可表达出第 i 种物品的数量范围

# 通过二进制优化，可以将「完全背包问题」转化为「0-1 背包问题」
# 经过「二进制优化」之后，算法的时间复杂度从 O(W*sum(count[i])) 降到了 O(W*sum(log_2count[i]))。
class Solution:
    # 思路 3：动态规划 + 二进制优化
    def multiplePackMethod1(self, weight: list[int], value: list[int], count: list[int], W: int):
        weight_new, value_new = [], []
        
        # 二进制优化
        for i in range(len(weight)):
            cnt = count[i]
            k = 1
            while k <= cnt:
                cnt -= k
                weight_new.append(weight[i] * k)
                value_new.append(value[i] * k)
                k *= 2
            if cnt > 0:
                weight_new.append(weight[i] * cnt)
                value_new.append(value[i] * cnt)
        
        dp = [0 for _ in range(W + 1)]
        size = len(weight_new)
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight_new[i - 1] - 1, -1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight_new[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight_new[i - 1]] + value_new[i - 1])
                    
        return dp[W]


# 混合背包问题

# 混合背包问题其实就是将「0-1 背包问题」、「完全背包问题」和「多重背包问题」这 3 种背包问题综合起来，
# 有的是能取 1 件，有的能取无数件，有的只能取 count[i] 件。
# 其实只要理解了之前讲解的这 3 种背包问题的核心思想，只要将其合并在一起就可以了。

# 并且在「多重背包问题」中，我们曾经使用「二进制优化」的方式，将「多重背包问题」转换为「0-1 背包问题」，
# 那么在解决「混合背包问题」时，我们也可以先将「多重背包问题」转换为「0-1 背包问题」，
# 然后直接再区分是「0-1 背包问题」还是「完全背包问题」就可以了。

# 下述代码中，count[i]=-1代表数量只有1个，指0-1背包
# 个人感觉其实不用特别标注，用count[i]=1代表数量为1个更好

class Solution:
    def mixedPackMethod1(self, weight: list[int], value: list[int], count: list[int], W: int):
        weight_new, value_new, count_new = [], [], []
        
        # 二进制优化
        for i in range(len(weight)):
            cnt = count[i]
            # 多重背包问题，转为 0-1 背包问题
            if cnt > 0:
                k = 1
                while k <= cnt:
                    cnt -= k
                    weight_new.append(weight[i] * k)
                    value_new.append(value[i] * k)
                    count_new.append(1)
                    k *= 2
                if cnt > 0:
                    weight_new.append(weight[i] * cnt)
                    value_new.append(value[i] * cnt)
                    count_new.append(1)
            # 0-1 背包问题，直接添加
            elif cnt == -1:
                weight_new.append(weight[i])
                value_new.append(value[i])
                count_new.append(1)
            # 完全背包问题，标记并添加
            else:
                weight_new.append(weight[i])
                value_new.append(value[i])
                count_new.append(0)
                
        dp = [0 for _ in range(W + 1)]
        size = len(weight_new)
    
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 0-1 背包问题
            if count_new[i - 1] == 1:
                # 逆序枚举背包装载重量（避免状态值错误）
                for w in range(W, weight_new[i - 1] - 1, -1):
                    # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight_new[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                    dp[w] = max(dp[w], dp[w - weight_new[i - 1]] + value_new[i - 1])
            # 完全背包问题
            else:
                # 正序枚举背包装载重量
                for w in range(weight_new[i - 1], W + 1):
                    # dp[w] 取「前 i - 1 种物品装入载重为 w 的背包中的最大价值」与「前 i 种物品装入载重为 w - weight[i - 1] 的背包中，再装入 1 件第 i - 1 种物品所得的最大价值」两者中的最大值
                    dp[w] = max(dp[w], dp[w - weight_new[i - 1]] + value_new[i - 1])
                    
        return dp[W]


# 分组背包问题

# 有 n 组物品和一个最多能装重量为 W 的背包，第 i 组物品的件数为 group_count[i]，
# 第 i 组的第 j 个物品重量为 weight[i][j]，价值为 value[i][j]。
# 每组物品中最多只能选择 1 件物品装入背包。请问在总重量不超过背包载重上限的情况下，能装入背包的最大价值是多少？

class Solution:
    # 思路 1：动态规划 + 二维基本思路
    def groupPackMethod1(self, group_count: list[int], weight: list[list[int]], value: list[list[int]], W: int):
        size = len(group_count)
        dp = [[0 for _ in range(W + 1)] for _ in range(size + 1)]
        
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举第 i - 1 组物品能取个数
                dp[i][w] = dp[i - 1][w]
                for k in range(group_count[i - 1]):
                    if w >= weight[i - 1][k]:
                        # dp[i][w] 取所有 dp[i - 1][w - weight[i - 1][k]] + value[i - 1][k] 中最大值
                        dp[i][w] = max(dp[i][w], dp[i - 1][w - weight[i - 1][k]] + value[i - 1][k])

# 分组背包问题的滚动数组优化

class Solution:
    # 思路 2：动态规划 + 滚动数组优化
    def groupPackMethod2(self, group_count: list[int], weight: list[list[int]], value: list[list[int]], W: int):
        size = len(group_count)
        dp = [0 for _ in range(W + 1)]
        
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量
            for w in range(W, -1, -1):
                # 枚举第 i - 1 组物品能取个数
                for k in range(group_count[i - 1]):
                    if w >= weight[i - 1][k]:
                        # dp[w] 取所有 dp[w - weight[i - 1][k]] + value[i - 1][k] 中最大值
                        dp[w] = max(dp[w], dp[w - weight[i - 1][k]] + value[i - 1][k])
                        
        return dp[W]

# 二维费用背包问题

# 有 n 件物品和有一个最多能装重量为 W、容量为 V 的背包。
# 第 i 件物品的重量为 weight[i]，体积为 volume[i]，价值为 value[i]，每件物品有且只有 1 件。
# 请问在总重量不超过背包载重上限、容量上限的情况下，能装入背包的最大价值是多少？

# 我们可以参考「0-1 背包问题」的状态定义和基本思路，
# 在「0-1 背包问题」基本思路的基础上，增加一个维度用于表示物品的容量。

class Solution:
    # 思路 1：动态规划 + 三维基本思路
    def twoDCostPackMethod1(self, weight: list[int], volume: list[int], value: list[int], W: int, V: int):
        size = len(weight)
        dp = [[[0 for _ in range(V + 1)] for _ in range(W + 1)] for _ in range(size + 1)]
    
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 枚举背包装载重量
            for w in range(W + 1):
                # 枚举背包装载容量
                for v in range(V + 1):
                    # 第 i - 1 件物品装不下
                    if w < weight[i - 1] or v < volume[i - 1]:
                        # dp[i][w][v] 取「前 i - 1 件物品装入装载重量为 w、装载容量为 v 的背包中的最大价值」
                        dp[i][w][v] = dp[i - 1][w][v]
                    else:
                        # dp[i][w][v] 取所有 dp[w - weight[i - 1]][v - volume[i - 1]] + value[i - 1] 中最大值
                        dp[i][w][v] = max(dp[i - 1][w][v], dp[i - 1][w - weight[i - 1]][v - volume[i - 1]] + value[i - 1])
                        
        return dp[size][W][V]

# 注意：采用上面的三维方式的「状态定义」和「状态转移方程」，往往会导致内存超出要求限制，
# 所以一般我们会采用「滚动数组」对算法的空间复杂度进行优化。

# 二维费用背包问题滚动数组优化

class Solution:        
    # 思路 2：动态规划 + 滚动数组优化
    def twoDCostPackMethod2(self, weight: list[int], volume: list[int], value: list[int], W: int, V: int):
        size = len(weight)
        dp = [[0 for _ in range(V + 1)] for _ in range(W + 1)]
        
        # 枚举前 i 组物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量
            for w in range(W, weight[i - 1] - 1, -1):
                # 逆序枚举背包装载容量
                for v in range(V, volume[i - 1] - 1, -1):
                    # dp[w][v] 取所有 dp[w - weight[i - 1]][v - volume[i - 1]] + value[i - 1] 中最大值
                    dp[w][v] = max(dp[w][v], dp[w - weight[i - 1]][v - volume[i - 1]] + value[i - 1])
                    
        return dp[W][V]


# 背包问题变种

# 1. 求恰好装满背包的最大价值

# 在给定背包重量 W，每件物品重量 weight[i]，物品间相互关系（分组、依赖等）的背包问题中，
# 请问在恰好装满背包的情况下，能装入背包的最大价值总和是多少？

# 如果题目要求「恰好装满背包」，则我们可在原有状态定义、状态转移方程的基础上，
# 在初始化时，令 dp[0]=0，以及 d[w]=−∞,1≤w≤W。 这样就可以保证最终得到的 dp[W] 为恰好装满背包的最大价值总和。

# 这是因为：
# 初始化的 dp 数组实际上就是在没有任何物品可以放入背包时的「合法状态」。
# 如果不要求恰好装满背包，那么：
#   任何载重上限下的背包，在不放入任何物品时，都有一个合法解，此时背包所含物品的最大价值为 0，即 dp[w]=0,0≤w≤W。
# 而如果要求恰好装满背包，那么：
#   1. 只有载重上限为 0 的背包，在不放入物品时，能够恰好装满背包（有合法解），
#      此时背包所含物品的最大价值为 0，即 dp[0]=0。
#   2. 其他载重上限下的背包，在放入物品的时，都不能恰好装满背包（都没有合法解），
#      此时背包所含物品的最大价值属于未定义状态，值应为 −∞，即 dp[w]=−∞,0≤w≤W。
# 我们可以通过判断 dp[w] 与 −∞ 的关系，来判断是否能恰好装满背包。

# 0-1 背包问题求恰好装满背包的最大价值
class Solution:
    # 0-1 背包问题 求恰好装满背包的最大价值
    def zeroOnePackJustFillUp(self, weight: list[int], value: list[int], W: int):
        size = len(weight)
        dp = [float('-inf') for _ in range(W + 1)]
        dp[0] = 0
        
        # 枚举前 i 种物品
        for i in range(1, size + 1):
            # 逆序枚举背包装载重量（避免状态值错误）
            for w in range(W, weight[i - 1] - 1, -1):
                # dp[w] 取「前 i - 1 件物品装入载重为 w 的背包中的最大价值」与「前 i - 1 件物品装入载重为 w - weight[i - 1] 的背包中，再装入第 i - 1 物品所得的最大价值」两者中的最大值
                dp[w] = max(dp[w], dp[w - weight[i - 1]] + value[i - 1])
        
        if dp[W] == float('-inf'):
            return -1
        return dp[W]