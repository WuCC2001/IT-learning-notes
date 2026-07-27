# 贪心算法适用于一类特殊问题：只要每一步都做出当前最优选择，最终就能得到整体最优解或近似最优解。
# 但并非所有问题都适用贪心算法。

# 通常，能用贪心算法解决的问题需同时满足两个条件：
# 1.贪心选择性质：
# 全局最优解可以通过一系列局部最优（贪心）选择获得。
# 贪心算法的每一步可能依赖之前的选择，但不会回溯，也不依赖未来的选择或子问题的解。
# 2.最优子结构：
# 问题的最优解包含其子问题的最优解。
# 如果原问题的最优解可以由子问题的最优解推导出来，则说明满足最优子结构；反之，则不满足，不能用贪心算法。

# 贪心算法正确性的证明
# 1. 数学归纳法
# 2. 交换论证法：假设存在更优解，通过交换局部选择，如果不会得到更优结果，则当前贪心解为最优。
# 3. 直觉思路上，验证局部最优能否推出全局最优（最优子结构）；或尝试构造反例

# 步骤：
# 问题转化：将原始优化问题转化为可以应用贪心策略的问题，明确每一步都可以做出一个局部最优的选择。
# 贪心策略制定：结合题意，选定合适的度量标准，设计出每一步的贪心选择规则，即在当前状态下选择最优（最有利）的方案，获得局部最优解。
# 最优子结构利用：保证每次贪心选择后，剩余子问题仍满足同样的结构和贪心选择性质，将每一步的局部最优解累积，最终合成原问题的全局最优解。

class Solution:
    # 分发饼干
    def findContentChildren(self, g: list[int], s: list[int]) -> int:
        s = sorted(s)[::-1]
        g = sorted(g)[::-1]
        p, q = 0, 0

        while p < len(s) and q < len(g):
            if s[p] >= g[q]:
                p += 1
                q += 1
            else:
                q += 1

        return p

    # 这个程序中的算法思路无法保证贪心的最优子结构
    # 具体而言，按照重叠区间的数量大小顺序构造，无法保证贪心的最优子结构
    # def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
    #     # 判断是否重叠的函数
    #     def _isOverlap_(m:list[int], n:list[int]) -> bool:
    #         if m[0] <= n[0] and m[1] > n[0]:
    #             return True
    #         elif m[0] > n[0] and m[0] < n[1]:
    #             return True
    #         else:
    #             return False

    #     def _valuesNum_(d:dict) -> int:
    #         n = 0
    #         for k, v in d.items():
    #             n += len(v)
    #         return n
        
    #     n = len(intervals)
    #     dictOverlap = {}
    #     for i in range(n):
    #         for j in range(i+1, n):
    #             # 如果2个区间重叠，则在字典中标记
    #             if _isOverlap_(intervals[i], intervals[j]):
    #                 if i in dictOverlap:
    #                     dictOverlap[i].add(j)  
    #                 else:
    #                     dictOverlap[i] = set()
    #                     dictOverlap[i].add(j)
    #                 if j in dictOverlap:
    #                     dictOverlap[j].add(i)
    #                 else:
    #                     dictOverlap[j] = set()
    #                     dictOverlap[j].add(i)

    #     # 按照重叠的区间数量排序
    #     print(dictOverlap)
    #     cnt = 0
    #     while _valuesNum_(dictOverlap):
    #         # 排序
    #         dictOverlap = dict(sorted(dictOverlap.items(), key = lambda x: len(x[1]), reverse = True))
    #         # 每次删除重叠区间数量最多的区间
    #         keyMaxOverlap = list(dictOverlap.keys())[0]
    #         dictOverlap.pop(keyMaxOverlap)
    #         print(keyMaxOverlap)
    #         cnt += 1
    #         # 把该区间在其他区间key下的value中删除
    #         for k in dictOverlap.keys():
    #             dictOverlap[k].discard(keyMaxOverlap)

    #     return cnt

    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        # 判断是否重叠的函数
        def _isOverlap_(m:list[int], n:list[int]) -> bool:
            # 假定 m[0] <= n[0]
            if m[1] > n[0]:
                return True
            else:
                return False

        # 按左端数值大小排序
        n = len(intervals)
        intervals.sort(key=lambda x: x[0])

        # 遍历，比较相邻2个区间的重叠情况
        p = 0
        while p < len(intervals)-1:
            i1, i2 = intervals[p], intervals[p+1]
            # 如果相邻的2个区间有重叠
            if _isOverlap_(i1, i2):
                # 删除最右侧更右（最大值更大）的区间
                if i1[1] <= i2[1]:
                    intervals.pop(p+1)
                else:
                    intervals.pop(p)
            # 没有重叠指针移动
            else:
                p += 1

        return n-p-1


s = Solution()
intervals = [[1,2],[2,3],[3,4],[1,3]]
intervals = [ [1,2], [1,2], [1,2] ]
intervals = [ [1,2], [2,3] ]
intervals = [[0,2],[1,3],[2,4],[3,5],[4,6]]
n = s.eraseOverlapIntervals(intervals)
print(n)