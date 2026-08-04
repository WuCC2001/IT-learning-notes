
# 记忆化搜索（Memoization Search）：
# 是一种通过存储已经遍历过的状态信息，从而避免对同一状态重复遍历的搜索算法。
# 记忆化搜索是动态规划的一种实现方式。在记忆化搜索中，当算法需要计算某个子问题的结果时，它首先检查是否已经计算过该问题。
# 如果已经计算过，则直接返回已经存储的结果；否则，计算该问题，并将结果存储下来以备将来使用。


# 记忆化搜索与递推区别
# 记忆化搜索：「自顶向下」的解决问题，采用自然的递归方式编写过程，在过程中会保存每个子问题的解（通常保存在一个数组或哈希表中）来避免重复计算。
#   - 优点：代码清晰易懂，可以有效的处理一些复杂的状态转移方程。有些状态转移方程是非常复杂的，
#     使用记忆化搜索可以将复杂的状态转移方程拆分成多个子问题，通过递归调用来解决。
#   - 缺点：可能会因为递归深度过大而导致栈溢出问题。
# 递推：「自底向上」的解决问题，采用循环的方式编写过程，在过程中通过保存每个子问题的解（通常保存在一个数组或哈希表中）来避免重复计算。
#   - 优点：避免了深度过大问题，不存在栈溢出问题。计算顺序比较明确，易于实现。
#   - 缺点：无法处理一些复杂的状态转移方程。有些状态转移方程非常复杂，如果使用递推方法来计算，就会导致代码实现变得非常困难。


# 根据记忆化搜索和递推的优缺点，我们可以在不同场景下使用这两种方法。

# 适合使用「记忆化搜索」的场景：
# 问题的状态转移方程比较复杂，递推关系不是很明确。
# 问题适合转换为递归形式，并且递归深度不会太深。

# 适合使用「递推」的场景：
# 问题的状态转移方程比较简单，递归关系比较明确。
# 问题不太适合转换为递归形式，或者递归深度过大容易导致栈溢出。


# 记忆化搜索解题步骤
# 我们在使用记忆化搜索解决问题的时候，其基本步骤如下：
# 1. 写出问题的动态规划「状态」和「状态转移方程」。
# 2. 定义一个缓存（数组或哈希表），用于保存子问题的解。
# 3. 定义一个递归函数，用于解决问题。在递归函数中，首先检查缓存中是否已经存在需要计算的结果，如果存在则直接返回结果，否则进行计算，并将结果存储到缓存中，再返回结果。
# 4. 在主函数中，调用递归函数并返回结果。

# 目标和，与将数组划分成和相等的2个子集，属于同一类题目
# 直接递归，超时
def findTargetSumWays(nums: list[int], target: int) -> int: 

    def TargetSumWays(n:int):
        if n == 0:
            return [0]
        
        memo = TargetSumWays(n-1)
        ways = []
        for m in memo:
            ways.append(m+nums[n-1])
            ways.append(m-nums[n-1])

        return ways

    memos = TargetSumWays(len(nums))
    cnt = 0
    for m in memos:
        if m == target:
            cnt += 1
    return cnt

def findTargetSumWays(nums: list[int], target: int) -> int:
    # 用来存储索引为n、当前和为curSum的、满足总和为target的组合数量
    dp = dict()

    def TargetSumWays(n:int, curSum:int):
        if n == -1:
            if curSum == target:
                return 1
            else:
                return 0

        if (n, curSum) in dp:
            return dp[(n, curSum)]

        dp[(n, curSum)] = TargetSumWays(n-1, curSum-nums[n]) + TargetSumWays(n-1, curSum+nums[n])
        return dp[((n, curSum))]

    return TargetSumWays(len(nums)-1, 0)

nums = [1,1,1,1,1]
target = 3
nums = [22,25,21,8,32,36,26,22,12,26,32,1,11,21,19,50,2,1,19,32]
target = 24
memos = findTargetSumWays(nums, target)
print(memos)