
# 链表的基本操作

# 1. 链表的结构定义

# 链节点类
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val      # 节点的值
        self.next = next    # 指向下一个节点

class LinkedList:
    def __init__(self):
        self.head = None    # 链表头指针，初始为 None

# 2. 创建链表：根据给定的线性表数据，依次生成链表节点，并将它们顺序连接起来，构成完整的链表。

# 根据 data 列表初始化一个新链表
def create(self, data):
    if not data:
        # 如果输入数据为空，直接返回，不创建链表
        return
    # 创建头节点，并将 head 指向头节点
    self.head = ListNode(data[0])
    cur = self.head  # cur 用于指向当前链表的尾节点
    # 依次遍历 data 中剩余的元素，逐个创建新节点并连接到链表尾部
    for i in range(1, len(data)):
        node = ListNode(data[i])  # 创建新节点
        cur.next = node           # 将新节点连接到当前尾节点
        cur = cur.next            # cur 指向新的尾节点，准备连接下一个节点

# 3. 链表长度
# 通过一个指针变量 cur 沿着链表的 next 指针逐个遍历节点，并用计数器 count 统计节点数量，最终得到链表长度。

# 获取线性链表长度
def length(self):
    count = 0                # 初始化计数器，记录节点个数
    cur = self.head          # 从链表头节点开始遍历
    while cur:               # 只要当前节点不为 None，就继续遍历
        count += 1           # 每遍历到一个节点，计数器加 1
        cur = cur.next       # 指针后移，指向下一个节点
    return count             # 返回计数器的值，即链表长度

# 4. 链表中查找值为 val 的节点

# 链表中查找值为 val 的节点
def find(self, val):
    cur = self.head  # 从链表头节点开始遍历
    while cur:  # 只要当前节点不为 None，就继续遍历
        if val == cur.val:  # 如果当前节点的值等于目标值，查找成功
            return cur      # 返回当前节点
        cur = cur.next      # 指针后移，指向下一个节点

    # 遍历完整个链表都没有找到目标值，返回 None
    return None

# 5. 插入节点：在链表的第 i 个位置前插入一个值为 val 的新节点。

# 插入节点
def insertInside(self, index, val):
    # 头部插入（index == 1）
    if index == 1:
        node = ListNode(val)
        node.next = self.head
        self.head = node
        return

    count = 0
    cur = self.head
    # 遍历链表，找到第 index - 1 个节点（即新节点的前驱节点）
    while cur and count < index - 1:
        cur = cur.next
        count += 1

    # 如果遍历到链表末尾还没找到前驱节点，说明 index 越界，插入失败
    if not cur:
        return 'Error'

    node = ListNode(val)
    # 尾部插入（index 指向最后一个节点的下一个位置）
    if cur.next is None:
        cur.next = node
    else:
        node.next = cur.next
        cur.next = node

# 6. 改变节点：将链表中第 i 个节点的值修改为 val

# 改变元素：将链表中第 i 个元素值改为 val
def change(self, index, val):
    # 初始化计数器 count 和指针 cur，cur 指向链表头节点
    count = 0
    cur = self.head
    # 遍历链表，直到找到第 index 个节点
    while cur and count < index:
        count += 1
        cur = cur.next
        
    # 如果 cur 为空，说明 index 越界，返回错误
    if not cur:
        return 'Error'

    # 修改第 index 个节点的值为 val
    cur.val = val

# 7. 删除元素：删除链表中第 i 个节点。

# 链表删除元素
def removeInside(self, index):
    # 初始化计数器 count 和指针 cur，cur 指向链表头节点
    count = 0
    cur = self.head

    # 遍历链表，cur 移动到第 index - 1 个节点（即待删除节点的前驱）
    while cur.next and count < index - 1:
        count += 1
        cur = cur.next

    # 如果 cur 为空，说明 index 越界，返回错误
    if not cur:
        return 'Error'

    # del_node 指向待删除的节点
    del_node = cur.next
    # 将 cur 的 next 指针指向 del_node 的下一个节点，实现删除
    cur.next = del_node.next


# 总结

# 链表特点
# 链表是一种链式存储的线性表数据结构，具有以下核心特征：
# 存储方式：通过指针连接任意存储单元，物理存储非连续
# 节点结构：每个节点包含数据域和指针域
# 访问方式：只能顺序访问，不支持随机访问

# 应用场景
# 频繁插入删除：链表在插入删除操作上比数组更高效
# 动态内存管理：适合内存大小不确定的场景
# 实现其他数据结构：栈、队列、哈希表等的基础
# 算法优化：某些算法中链表结构能提供更好的性能