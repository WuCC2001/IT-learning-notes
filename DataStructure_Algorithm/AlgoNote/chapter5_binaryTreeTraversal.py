# 二叉树前中后序遍历的非递归实现

# 前序遍历的访问顺序为：根节点 → 左子树 → 右子树。由于栈具有「后进先出」的特性，为了保证遍历顺序正确，
# 入栈时应先将右子节点压入，再将左子节点压入，这样弹出时会先访问左子树，再访问右子树。

# 具体实现步骤如下：
# 1. 如果二叉树为空，直接返回。
# 2. 初始化一个栈，将根节点压入栈中。
# 3. 当栈不为空时，重复以下操作：
#   1. 弹出栈顶节点 node，访问该节点。
#   2. 如果 node 的右子节点存在，则将其压入栈中。
#   3. 如果 node 的左子节点存在，则将其压入栈中。

class Solution:
    def preorderTraversal(self, root) -> list[int]:
        if not root:
            return

        res = []
        stack = [root]

        while stack:
            node = stack.pop()
            res.append(node.val)
            # 注意：先右后左，保证左子树先被遍历
            if node.right:
                stack.append(node.right)
            if node.left:
                stack.append(node.left)

        return res


# 与前序遍历不同，中序遍历要求在访问根节点前，必须先遍历完其左子树。
# 因此，只有在左子树全部出栈后，当前节点才能出栈并被访问。

# 具体做法是：从根节点出发，不断将当前节点压入栈中，并向左移动，直到没有左子节点为止。
# 此时弹出栈顶节点，访问该节点，然后转向其右子树，重复上述过程。这样可以确保遍历顺序严格按照「左-根-右」进行。

# 中序遍历的非递归（显式栈）实现步骤如下：
# 1. 如果二叉树为空，直接返回。
# 2. 初始化一个空栈。
# 3. 当当前节点不为空或栈不为空时，重复以下操作：
#   1. 如果当前节点不为空，不断将其压入栈，并向左移动，直到左子节点为空。
#   2. 如果当前节点为空，说明已到达最左侧，弹出栈顶节点node，访问该节点，然后将当前节点指向 node 的右子节点，继续上述循环。

class Solution:
    def inorderTraversal(self, root) -> list[int]:
        if not root:
            return

        res = []
        stack = []
        cur = root

        while cur or stack:
            # 不断向左子树深入，将沿途节点全部入栈
            while cur:
                stack.append(cur)
                cur = cur.left
            
            # 此时已到达最左侧，弹出栈顶节点
            node = stack.pop()
            res.append(node.val)
            cur = node.right  # 转向右子树，继续上述过程

        return res


# 后序遍历要求在左右子树都访问完成后，才能访问根节点。因此，必须确保：
# 当前节点在其左右孩子节点都访问完毕之前不能出栈。

# 后序遍历的非递归实现可以通过如下方式优化理解：
# 1. 从根节点出发，将其依次压入栈中，并不断向左深入，直到到达最左侧节点。
# 2. 每次弹出栈顶节点，判断其右子树是否已被访问（用 prev 记录上一个访问的节点）：
#   1. 如果已访问，则访问该节点；
#   2. 如果未访问，则将该节点重新压入栈，并转而遍历其右子树。

class Solution:
    def postorderTraversal(self, root) -> list[int]:
        # if not root:
        #     return

        res = []
        stack = []
        cur = root
        prev = None

        while cur or stack:
            # 不断向左子树深入，将沿途节点全部入栈
            while cur:
                stack.append(cur)
                cur = cur.left
            
            node = stack.pop()
            # 如果没有右子树，或右子树已经被访问过
            if not node.right or prev == node.right:
                res.append(node.val)
                # 更新上一次访问的节点
                prev = node
            # 如果右子树还没被访问
            else:
                # 当前节点重新入栈，转而遍历右子树
                stack.append(node)
                cur = node.right

        return res

# 二叉树层序遍历（Level Order Traversal）

# 1. 如果二叉树为空，直接返回。
# 2. 将根节点加入队列。
# 3. 当队列不为空时，重复以下操作：
#   1. 记录当前队列长度 si （即当前层的节点数）。
#   2. 依次从队列中取出这 si 个节点，访问它们，并将它们的左右子节点（如存在）加入队列。
#   3. 队列为空时，遍历结束。

class Solution:
    def levelOrder(self, root) -> list[list[int]]:
        """
        二叉树层序遍历（广度优先搜索，BFS）
        返回每一层的节点值组成的二维列表
        """
        if not root:
            return []  # 空树直接返回空列表

        from collections import deque  # 推荐使用 deque 提高队列效率
        queue = deque([root])  # 初始化队列，根节点入队
        order = []             # 用于存储最终结果

        while queue:
            level = []                 # 存储当前层的节点值
            size = len(queue)          # 当前层的节点数量
            for _ in range(size):
                curr = queue.popleft() # 弹出队首节点
                level.append(curr.val) # 访问当前节点
                if curr.left:
                    queue.append(curr.left)   # 左子节点入队
                if curr.right:
                    queue.append(curr.right)  # 右子节点入队

            order.append(level)     # 当前层结果加入总结果

        return order

# 4种遍历方法的复杂度

# 遍历方式	空间复杂度	时间复杂度
# 前序遍历	    O(h)	O(n)
# 中序遍历	    O(h)	O(n)
# 后序遍历	    O(h)	O(n)
# 层序遍历	    O(w)	O(n)
# 注：h 为树的高度，w 为树的最大宽度，n 为节点总数
# 对于深度很大的树，前中后序遍历（递归）可能导致栈溢出；对于宽度很大的树，层序遍历的空间复杂度可能较高
# 空间复杂度理解（显式栈实现）：前序遍历的复杂度源自于树的层级分叉，中序后序遍历的复杂度源自于树的深度

# 4种遍历方法的应用和注意

# 前序遍历：
# 适合需要先处理根节点再处理子节点的场景
# 常用于树的复制、序列化等操作

# 中序遍历
# 对于二叉搜索树，中序遍历得到有序序列
# 适合需要按顺序处理节点的场景

# 后序遍历
# 适合需要先处理子节点再处理父节点的场景
# 常用于树的删除、后序表达式计算等

# 层序遍历
# 适合需要按层处理节点的场景