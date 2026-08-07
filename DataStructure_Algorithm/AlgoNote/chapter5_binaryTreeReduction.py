# 二叉树的还原
# 指通过已知的二叉树遍历序列，重建出原始的二叉树结构。

# 我们知道，对于一棵非空二叉树，其前序、中序、后序遍历序列都是唯一的。
# 但反过来，如果只给出某一种遍历序列，是否能唯一确定这棵二叉树呢？答案是否定的。

# 两种遍历序列的组合情况
# 前序 + 中序：前序序列确定根节点，中序序列确定左右子树的范围。递归分割子序列，可以唯一还原原二叉树。
# 中序 + 后序：后序序列确定根节点，中序序列确定左右子树的范围，方法与前序+中序类似，也能唯一还原二叉树。
# 中序 + 层序：通过层序遍历确定每个子树的根节点，再结合中序遍历分割左右子树，也可以唯一还原二叉树。

# 不能唯一还原的特殊情况
# 前序 + 后序：仅有前序和后序遍历序列时，无法唯一确定二叉树结构。因为缺少中序信息，无法区分左右子树的分界。
# 例如，如果存在度为 1 的节点，无法判断该节点是左子树还是右子树。
# 特殊说明：只有当二叉树中每个节点的度均为 2 或 0（即满二叉树）时，前序和后序遍历序列才能唯一确定二叉树。
# 如果存在度为 1 的节点，则无法唯一还原。

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

# 利用前序与中序遍历序列重建二叉树

# 简要流程如下：
# 取前序序列首元素作为根节点。
# 在中序序列中定位根节点，分割出左、右子树的中序区间。
# 根据左子树节点数，切分前序序列为左、右子树区间。
# 递归处理左右子树，直至区间为空。

class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode:
        """
        根据前序遍历和中序遍历序列重建二叉树

        参数:
            preorder: List[int]，二叉树的前序遍历序列
            inorder: List[int]，二叉树的中序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(preorder, inorder, n):
            """
            递归构建二叉树

            参数:
                preorder: 当前子树的前序遍历序列
                inorder: 当前子树的中序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为 0
            # 在中序遍历中查找根节点位置
            k = 0
            while preorder[0] != inorder[k]:
                k += 1
            # 创建根节点
            node = TreeNode(inorder[k])
            # 递归构建左子树
            node.left = createTree(preorder[1: k + 1], inorder[0: k], k)
            # 递归构建右子树
            node.right = createTree(preorder[k + 1:], inorder[k + 1:], n - k - 1)
            return node

        # 从整棵树的前序和中序序列开始递归构建
        return createTree(preorder, inorder, len(inorder))

# 利用中序与后序遍历序列重建二叉树

# 具体步骤如下：
# 后序遍历序列的最后一个元素postorder[-1]为当前子树的根节点。
# 在中序遍历序列中查找该根节点的位置inorder[k]，据此将中序序列分为左、右子树区间，并确定左右子树的节点数。
# 利用左右子树的节点数，将后序遍历序列划分为左、右子树对应的区间。
# 构建当前根节点，并递归构建其左、右子树，直到区间为空为止。

class Solution:
    def buildTree(self, inorder: list[int], postorder: list[int]) -> TreeNode:
        """
        根据中序遍历和后序遍历序列重建二叉树

        参数:
            inorder: List[int]，二叉树的中序遍历序列
            postorder: List[int]，二叉树的后序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(inorder, postorder, n):
            """
            递归构建二叉树

            参数:
                inorder: 当前子树的中序遍历序列
                postorder: 当前子树的后序遍历序列
                n: 当前子树的节点数
            返回:
                TreeNode，当前子树的根节点
            """
            if n == 0:
                return None  # 递归终止条件：子树节点数为0，返回空节点

            # 后序遍历的最后一个元素为当前子树的根节点
            root_val = postorder[n - 1]
            # 在中序遍历中查找根节点的位置
            k = 0
            while inorder[k] != root_val:
                k += 1

            # 创建根节点
            node = TreeNode(root_val)
            # 递归构建左子树
            # 左子树的中序区间：inorder[0:k]
            # 左子树的后序区间：postorder[0:k]
            node.left = createTree(inorder[0:k], postorder[0:k], k)
            # 递归构建右子树
            # 右子树的中序区间：inorder[k+1:n]
            # 右子树的后序区间：postorder[k:n-1]
            node.right = createTree(inorder[k+1:n], postorder[k:n-1], n - k - 1)
            return node

        # 从整棵树的中序和后序序列开始递归构建
        return createTree(inorder, postorder, len(postorder))

# 利用前序与后序遍历序列构造二叉树

# 实现思路与步骤
# 我们可以假定前序遍历序列的第二个元素为左子树的根节点，进而递归划分左右子树。具体步骤如下：
# 前序遍历的第一个元素preorder[0]是当前子树的根节点。
# 前序遍历的第二个元素preorder[1]是左子树的根节点。我们在后序遍历中查找该节点的位置postorder[k]，该位置左侧为左子树，右侧为右子树。
# 由 k 可确定左子树的节点数量，从而划分前序和后序序列的左右子树部分。
# 递归构建当前节点的左、右子树，直到子树为空。

class Solution:
    def constructFromPrePost(self, preorder: list[int], postorder: list[int]) -> TreeNode:
        """
        根据前序和后序遍历序列构造二叉树（不唯一）
        参数:
            preorder: List[int]，二叉树的前序遍历序列
            postorder: List[int]，二叉树的后序遍历序列
        返回:
            TreeNode，重建后的二叉树根节点
        """
        def createTree(preorder, postorder, n):
            if n == 0:
                return None  # 递归终止条件：子树节点数为0，返回空节点
            # 前序遍历的第一个元素为当前子树的根节点
            root_val = preorder[0]
            node = TreeNode(root_val)
            if n == 1:
                return node  # 只有一个节点，直接返回
            # 前序遍历的第二个元素为左子树的根节点
            left_root_val = preorder[1]
            # 在后序遍历中查找左子树根节点的位置
            k = 0
            while postorder[k] != left_root_val:
                k += 1
            # k 为左子树在 postorder 中的结尾索引，左子树节点数为 k+1
            # 划分左右子树的前序和后序区间
            # 左子树：preorder[1:k+2], postorder[0:k+1]
            # 右子树：preorder[k+2:], postorder[k+1:n-1]
            node.left = createTree(preorder[1:k+2], postorder[0:k+1], k+1)
            # TODO
            # 代码有误，长度应该是 n-k-2
            node.right = createTree(preorder[k+2:], postorder[k+1:n-1], n-k-2)
            return node
        # 从整棵树的前序和后序序列开始递归构建
        return createTree(preorder, postorder, len(preorder))