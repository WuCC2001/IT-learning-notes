
# 计数排序（Counting Sort）基本思想：

# 统计数组中每个元素出现的次数，然后根据统计信息将元素按顺序放置到正确位置，实现排序。

# 计数排序算法步骤
    # 确定数值范围：找出数组中的最大值和最小值，计算数值范围。
    # 创建计数数组：创建一个大小为数值范围的数组，用于统计每个元素出现的次数。
    # 统计元素频次：遍历原数组，统计每个元素出现的次数。
    # 计算累积频次：将计数数组转换为累积频次数组，表示每个元素在排序后数组中的位置。
    # 逆序填充结果：逆序遍历原数组，根据累积频次将元素放入正确位置。

# 通过逆序填充结果，保证排序的稳定性

class Solution:
    def countingSort(self, nums: list[int]) -> list[int]:
        # 确定数值范围
        nums_min, nums_max = min(nums), max(nums)
        size = nums_max - nums_min + 1
        counts = [0 for _ in range(size)]
        
        # 统计每个元素出现的次数
        for num in nums:
            counts[num - nums_min] += 1
        
        # 计算累积频次（每个元素出现的次数）
        for i in range(1, size):
            counts[i] += counts[i - 1]

        # 逆序填充结果数组
        res = [0 for _ in range(len(nums))]
        for i in range(len(nums) - 1, -1, -1):
            num = nums[i]
            # 根据累积计数数组，将 num 放在数组对应位置
            res[counts[num - nums_min] - 1] = num
            counts[num - nums_min] -= 1

        return res

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.countingSort(nums)

# 计数排序是一种非比较排序算法，通过统计元素频次实现排序。它特别适合数值范围较小的整数排序。
# 优点：时间复杂度稳定，稳定排序，适合小范围整数排序
# 缺点：空间复杂度与数值范围相关，不适合大范围数值


# 桶排序（Bucket Sort）：

# 将待排序元素分散到多个桶中，对每个桶单独排序后合并。

# 桶排序算法步骤
    # 确定桶的数量：根据待排序数组的数值范围，将其划分为 k 个桶，每个桶对应一个特定的区间。
    # 元素分配：遍历数组，将每个元素根据其数值映射到所属的桶中。
    # 桶内排序：对每个非空桶分别进行排序（可选用插入排序、归并排序、快速排序等算法）。
    # 合并结果：按桶的顺序依次合并所有已排序的桶，得到最终有序数组。

class Solution:
    # 插入排序
    def insertionSort(self, nums: list[int]) -> list[int]:
        # 遍历无序区间
        for i in range(1, len(nums)):
            temp = nums[i]
            j = i
            # 从右至左遍历有序区间
            while j > 0 and nums[j - 1] > temp:
                # 将有序区间中插入位置右侧的元素依次右移一位
                nums[j] = nums[j - 1]
                j -= 1
            # 将该元素插入到适当位置
            nums[j] = temp
        return nums

    def bucketSort(self, nums: list[int], bucket_size=5) -> list[int]:
        # 计算数据范围
        nums_min, nums_max = min(nums), max(nums)
        bucket_count = (nums_max - nums_min) // bucket_size + 1
        # 定义桶数组 buckets
        buckets = [[] for _ in range(bucket_count)]

        # 遍历待排序数组元素，将每个元素根据大小分配到对应的桶中
        for num in nums:
            buckets[(num - nums_min) // bucket_size].append(num)

        # 排序并合并
        res = []
        for bucket in buckets:
            self.insertionSort(bucket)
            res.extend(bucket)
        
        # 返回结果数组
        return res

    def sortArray(self, nums: list[int]) -> list[int]:
        return self.bucketSort(nums)

# 桶排序是一种分布式排序算法，通过将数据分散到多个桶中，对每个桶单独排序后合并实现排序。
# 优点：数据分布均匀时效率高，适合外部排序，可并行处理
# 缺点：需要额外空间，数据分布不均匀时效率下降，对数据范围有要求


# 基数排序（Radix Sort）

# 基本思想：
# 按照数字的每一位进行排序，从最低位到最高位，逐位比较。

# 基数排序算法可以采用「最低位优先法（Least Significant Digit First）」或者「最高位优先法（Most Significant Digit first）」。
# 最常用的是「最低位优先法」。

# 「最低位优先法」步骤
    # 确定最大位数：遍历数组元素，找到数组中最大值的位数。
    # 从最低位（个位）开始，到最高位为止，逐位对每一位进行排序：
    # 创建 10 个桶（每个桶分别代表 0∼9 中的一个数字）。
    # 按照每个元素当前位上的数字，将元素放入对应桶中。
    # 清空原始数组，然后按照桶的顺序依次取出对应元素，重新加入到数组中。

# 每次按位排序，保证最后的整体结果是稳定的

class Solution:
    def radixSort(self, nums: list[int]) -> list[int]:
        # 获取最大位数
        size = len(str(max(nums)))
        
        # 从个位开始逐位排序
        for i in range(size):
            # 创建 10 个桶，每个桶分别代表 0 ~ 9 中的 1 个数字
            buckets = [[] for _ in range(10)]
            
            # 按当前位数字分桶
            for num in nums:
                buckets[num // (10 ** i) % 10].append(num)
            
            # 重新收集
            nums.clear()
            for bucket in buckets:
                for num in bucket:
                    nums.append(num)
                    
        # 完成排序，返回结果数组
        return nums
    
    def sortArray(self, nums: list[int]) -> list[int]:
        return self.radixSort(nums)

# 基数排序是一种非比较排序算法，通过按位分配和收集实现排序。
# 优点：时间复杂度与数据范围无关，稳定排序，适合固定位数数据（如电话号码、身份证号等）
# 缺点：空间复杂度较高，只适用于整数排序