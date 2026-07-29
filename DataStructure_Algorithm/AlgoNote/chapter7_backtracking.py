# 回溯算法（Backtracking）：
# 回溯算法是一种系统地搜索所有可能解的算法，通过递归和试错的方式逐步构建解的过程。
# 当发现当前路径无法满足题目要求或无法得到有效解时，算法会撤销上一步的选择（即「回溯」），
# 返回到上一个决策点，尝试其他可能的路径。回溯法的核心思想是「走不通就退回，换条路再试」，
# 而每次需要回退的节点称为「回溯点」。

# 回溯算法常用递归方式实现
# 回溯算法通用模板:
# def backtrack(参数):
#     if 终止条件:
#         处理结果
#         return
#     for 选择 in 可选列表:
#         if 满足约束:
#             做选择
#             backtrack(新参数)
#             撤销选择

# 回溯算法的核心思想是：
# 通过深度优先搜索，不断尝试所有可能的选择，当发现当前路径不满足条件时就回退（回溯），
# 尝试其他路径，最终找到所有可行解或最优解。

# 回溯算法的基本步骤如下：
# 1.明确所有选择：画出决策树，理清每一步有哪些可选项。每个节点的分支代表一次选择。
# 2.明确终止条件：终止条件通常是递归到某一深度、遍历完所有元素或满足题目要求。到达终止条件时，处理当前结果（如加入答案集）。
# 3.将决策树和终止条件转化为代码：
#   1.定义回溯函数（明确函数意义、传入参数、返回结果等）。
#   2.书写回溯函数主体（给出约束条件、选择元素、递归搜索、撤销选择部分）。
#   3.明确递归终止条件（给出递归终止条件，以及递归终止时的处理方法）。

def combinationSum2(candidates: list[int], target: int) -> list[list[int]]:
    res = []
    subset = []
    candidates.sort()

    def backtracking(k):
        if sum(subset) == target:
            res.append(subset[:])
            return

        if sum(subset) > target:
            return

        for i in range(k, len(candidates)):
            # 剪枝，同一组分支中如有重复元素，只保留第1个
            if i > k and candidates[i] == candidates[i-1]:
                continue
            subset.append(candidates[i])
            backtracking(i+1)
            subset.pop()
    backtracking(0)

    return res

candidates = [10,1,2,7,6,1,5]
target = 8
candidates = [14,6,25,9,30,20,33,34,28,30,16,12,31,9,9,12,34,16,25,32,8,7,30,12,33,20,21,29,24,17,27,34,11,17,30,6,32,21,27,17,16,8,24,12,12,28,11,33,10,32,22,13,34,18,12]
target = 27
candidates = [2,5,2,1,2]
target = 5
print(combinationSum2(candidates, target))