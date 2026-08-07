# 二叉搜索树

# 二叉搜索树（Binary Search Tree, BST），又称二叉查找树、有序二叉树或排序二叉树，
# 是一种特殊的二叉树结构，满足以下性质：
# 对于任意节点，如果其左子树非空，则左子树所有节点的值均 小于 该节点的值；
# 对于任意节点，如果其右子树非空，则右子树所有节点的值均 大于 该节点的值；
# 任意节点的左右子树也都分别是二叉搜索树（递归定义）。

# 二叉搜索树的查找
# 基于二叉搜索树的性质，查找过程可以高效地缩小范围。
# 每次比较后，只需决定向左子树还是右子树继续查找，从而大大提升查找效率。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val      # 节点值
        self.left = left    # 左子节点
        self.right = right  # 右子节点

class Solution:
    def searchBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        在二叉搜索树中查找值为 val 的节点

        参数:
            root: TreeNode，二叉搜索树的根节点
            val: int，待查找的目标值
        返回:
            TreeNode，值为 val 的节点，如果未找到则返回 None
        """
        if not root:
            return None  # 空树或查找失败，返回 None

        if val == root.val:
            return root  # 找到目标节点，返回
        elif val < root.val:
            # 目标值小于当前节点值，递归查找左子树
            return self.searchBST(root.left, val)
        else:
            # 目标值大于当前节点值，递归查找右子树
            return self.searchBST(root.right, val)

# 指标	    复杂度	            说明
# 最优时间    O(log_2(N))     树接近完全平衡
# 最坏时间    O(N)            树退化为单链表，需遍历所有节点
# 平均时间    O(log_2(N))     随机插入情况下
# 空间复杂度  O(1)            递归实现时为O(height)，迭代实现为O(1)


# 二叉搜索树的插入
# 二叉搜索树的插入过程与查找类似
# 注意：二叉搜索树不允许重复节点。如果 val 已存在于树中，则不插入，直接返回原树。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # 节点值
        self.left = left        # 左子节点
        self.right = right      # 右子节点

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        在二叉搜索树中插入一个值为 val 的节点

        参数:
            root: TreeNode，二叉搜索树的根节点
            val: int，待插入的节点值
        返回:
            TreeNode，插入后的二叉搜索树根节点
        """
        if root is None:
            # 当前子树为空，直接创建新节点并返回
            return TreeNode(val)
        
        # 注意返回值的含义，其代表返回插入了节点之后的新子树
        if val < root.val:
            # 待插入值小于当前节点值，递归插入到左子树
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            # 待插入值大于当前节点值，递归插入到右子树
            root.right = self.insertIntoBST(root.right, val)
        # 如果 val == root.val，不插入（不允许重复），直接返回原树
        return root

# 二叉搜索树的创建

# 二叉搜索树的创建通常从一棵空树开始，依次将数组中的每个元素插入到树中，最终形成完整的二叉搜索树。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val          # 节点值
        self.left = left        # 左子节点
        self.right = right      # 右子节点

class Solution:
    def insertIntoBST(self, root: TreeNode, val: int) -> TreeNode:
        """
        在二叉搜索树中插入一个值为 val 的节点

        参数:
            root: TreeNode，二叉搜索树的根节点
            val: int，待插入的节点值
        返回:
            TreeNode，插入后的二叉搜索树根节点
        """
        if root is None:
            # 当前子树为空，直接创建新节点并返回
            return TreeNode(val)
        if val < root.val:
            # 待插入值小于当前节点值，递归插入到左子树
            root.left = self.insertIntoBST(root.left, val)
        elif val > root.val:
            # 待插入值大于当前节点值，递归插入到右子树
            root.right = self.insertIntoBST(root.right, val)
        # 如果 val == root.val，不插入（不允许重复），直接返回原树
        return root

    def buildBST(self, nums) -> TreeNode:
        """
        根据给定数组 nums 创建一棵二叉搜索树

        参数:
            nums: List[int]，待插入的节点值数组
        返回:
            TreeNode，构建好的二叉搜索树根节点
        """
        root = None  # 初始化根节点为空
        for num in nums:
            root = self.insertIntoBST(root, num)  # 依次插入每个元素
        return root

# 二叉搜索树的删除

# 删除操作算法步骤
# 在二叉搜索树中删除节点时，首先需要定位到目标节点，然后根据其子树情况分为三种情形：
#   左子树为空：用其右子树替代被删除节点的位置。
#   右子树为空：用其左子树替代被删除节点的位置。
#   左右子树均不为空：利用二叉搜索树的有序性，可用「直接前驱」或「直接后继」节点的值替换当前节点，然后递归删除前驱或后继节点。
#       直接前驱：即左子树中值最大的节点（左子树最右侧节点）。
#       直接后继：即右子树中值最小的节点（右子树最左侧节点）。

# 具体删除步骤如下：

# 如果当前节点为空，直接返回。
# 如果当前节点值大于 val ，递归在左子树中查找并删除，更新左子树。
# 如果当前节点值小于 val ，递归在右子树中查找并删除，更新右子树。
# 如果当前节点值等于 val ，即找到目标节点，分三种情况处理：
#   如果左子树为空，返回右子树（右子树顶替当前节点）。
#   如果右子树为空，返回左子树（左子树顶替当前节点）。
#   如果左右子树均不为空，将左子树整体接到右子树的最左侧节点下，然后返回右子树作为新的子树根节点。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root: TreeNode, val: int) -> TreeNode:
        """
        在二叉搜索树中删除值为 val 的节点，并返回新的根节点

        参数:
            root: TreeNode，当前子树的根节点
            val: int，待删除的节点值
        返回:
            TreeNode，删除节点后的新根节点
        """
        if not root:
            # 递归终止条件：未找到目标节点，直接返回
            return None

        if val < root.val:
            # 待删除值小于当前节点，递归去左子树删除
            root.left = self.deleteNode(root.left, val)
            return root
        elif val > root.val:
            # 待删除值大于当前节点，递归去右子树删除
            root.right = self.deleteNode(root.right, val)
            return root
        else:
            # 找到目标节点，分三种情况处理
            if not root.left:
                # 情况 1：左子树为空，直接返回右子树
                return root.right
            elif not root.right:
                # 情况 2：右子树为空，直接返回左子树
                return root.left
            else:
                # 情况 3：左右子树均不为空
                # 找到右子树的最左节点（即后继节点）
                successor = root.right
                while successor.left:
                    successor = successor.left
                # 用后继节点的值替换当前节点
                root.val = successor.val
                # 在右子树中递归删除后继节点
                root.right = self.deleteNode(root.right, successor.val)
                return root

# 基本操作算法分析
# 操作	最优时间	最坏时间	平均时间	空间复杂度
# 查找	O(log n)	O(n)	O(log n)	O(1)
# 插入	O(log n)	O(n)	O(log n)	O(1)
# 删除	O(log n)	O(n)	O(log n)	O(1)
# 说明：最优情况是树接近完全平衡，最坏情况是树退化为单链表。

# 算法特点
# 优点：
    # 查找、插入、删除效率高（平均 O(log n)）
    # 支持范围查询和有序遍历
    # 实现相对简单，易于理解
# 缺点：
    # 插入顺序影响树的高度和性能
    # 不平衡时可能退化为链表（O(n) 复杂度），需要额外的平衡机制（如 AVL 树、红黑树）