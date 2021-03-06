# LeetCode题解(1591)：奇怪的打印机II(Python)

题目：[原题链接](https://leetcode-cn.com/problems/strange-printer-ii/)（困难）

标签：贪心算法

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时     |
| -------------- | ---------- | ---------- | ------------ |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 132ms (100%) |
| Ans 2 (Python) |            |            |              |
| Ans 3 (Python) |            |            |              |

解法一：

```python
# 检查顺序合法性
class Order:
    class Node:
        def __init__(self, i):
            self.i = i
            self.children = []

    def __init__(self, n):
        self.n = n
        self.node_list = [self.Node(i) for i in range(n)]

    def add(self, since, to):
        if self._has_child(to, since):
            return False
        else:
            self.node_list[since].children.append(self.node_list[to])
            return True

    def _has_child(self, i, aim):
        waiting_nodes = collections.deque([self.node_list[i]])
        while waiting_nodes:
            node = waiting_nodes.popleft()
            for child in node.children:
                if child.i == aim:
                    return True
                waiting_nodes.append(child)
        return False


class Solution:
    def isPrintable(self, targetGrid: List[List[int]]) -> bool:
        # 遍历检查所有的颜色及颜色的最上、最下、最左、最右（依次）的位置
        # O(N×M)
        color_dict = {}
        m = len(targetGrid)
        n = len(targetGrid[0])
        for i in range(m):
            for j in range(n):
                color = targetGrid[i][j]
                if color not in color_dict:
                    color_dict[color] = [i, i, j, j]
                else:
                    color_dict[color][0] = min(color_dict[color][0], i)
                    color_dict[color][1] = max(color_dict[color][1], i)
                    color_dict[color][2] = min(color_dict[color][2], j)
                    color_dict[color][3] = max(color_dict[color][3], j)

        # 逐个检查每个颜色的打印顺序（即该颜色的区间范围内的数已经比它更晚打印）
        order_list = set()
        for color in color_dict:
            position = color_dict[color]
            for i in range(position[0], position[1] + 1):
                for j in range(position[2], position[3] + 1):
                    if targetGrid[i][j] != color:
                        order = (color, targetGrid[i][j])
                        if order not in order_list:
                            order_list.add(order)

        # print(order_list)

        # 检查顺序是否可能实现
        order_monitor = Order(61)
        for order in order_list:
            if not order_monitor.add(order[0], order[1]):
                return False

        return True
```