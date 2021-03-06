# LeetCode题解(1594)：矩阵从左上移动到右下的最大非负积(Python)

题目：[原题链接](https://leetcode-cn.com/problems/maximum-non-negative-product-in-a-matrix/)（中等）

标签：贪心算法、动态规划

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时   |
| -------------- | ---------- | ---------- | ---------- |
| Ans 1 (Python) | $O(N×M)$   | $O(N×M)$   | 44ms (98%) |
| Ans 2 (Python) |            |            |            |
| Ans 3 (Python) |            |            |            |

解法一（动态规划）：

```python
class Solution:
    def maxProductPath(self, grid: List[List[int]]) -> int:
        if not grid or not grid[0]:
            return -1

        N1, N2 = len(grid), len(grid[0])
        dp = [[(None, None)] * N2 for _ in range(N1)]
        if grid[0][0] > 0:
            dp[0][0] = (grid[0][0], None)
        elif grid[0][0] == 0:
            dp[0][0] = (0, 0)
        else:
            dp[0][0] = (None, grid[0][0])

        # 处理第1列
        for i in range(1, N1):
            if grid[i][0] > 0:
                n1 = dp[i - 1][0][0] * grid[i][0] if dp[i - 1][0][0] is not None else None
                n2 = dp[i - 1][0][1] * grid[i][0] if dp[i - 1][0][1] is not None else None
                dp[i][0] = (n1, n2)
            elif grid[i][0] == 0:
                dp[i][0] = (0, 0)
            else:
                n1 = dp[i - 1][0][1] * grid[i][0] if dp[i - 1][0][1] is not None else None
                n2 = dp[i - 1][0][0] * grid[i][0] if dp[i - 1][0][0] is not None else None
                dp[i][0] = (n1, n2)

        # 处理第1行
        for j in range(1, N2):
            if grid[0][j] > 0:
                n1 = dp[0][j - 1][0] * grid[0][j] if dp[0][j - 1][0] is not None else None
                n2 = dp[0][j - 1][1] * grid[0][j] if dp[0][j - 1][1] is not None else None
                dp[0][j] = (n1, n2)
            elif grid[0][j] == 0:
                dp[0][j] = (0, 0)
            else:
                n1 = dp[0][j - 1][1] * grid[0][j] if dp[0][j - 1][1] is not None else None
                n2 = dp[0][j - 1][0] * grid[0][j] if dp[0][j - 1][0] is not None else None
                dp[0][j] = (n1, n2)

        # 处理其他部分
        for i in range(1, N1):
            for j in range(1, N2):
                if grid[i][j] > 0:
                    n11 = dp[i - 1][j][0] * grid[i][j] if dp[i - 1][j][0] is not None else None
                    n12 = dp[i][j - 1][0] * grid[i][j] if dp[i][j - 1][0] is not None else None
                    if n11 is not None and n12 is not None:
                        n1 = max(n11, n12)
                    elif n11 is not None:
                        n1 = n11
                    elif n12 is not None:
                        n1 = n12
                    else:
                        n1 = None
                    n21 = dp[i - 1][j][1] * grid[i][j] if dp[i - 1][j][1] is not None else None
                    n22 = dp[i][j - 1][1] * grid[i][j] if dp[i][j - 1][1] is not None else None
                    if n21 is not None and n22 is not None:
                        n2 = min(n21, n22)
                    elif n21 is not None:
                        n2 = n21
                    elif n22 is not None:
                        n2 = n22
                    else:
                        n2 = None
                    # print("(", i, ",", j, ")", grid[i][j], "->", n11, n12, n21, n22)
                    dp[i][j] = (n1, n2)
                elif grid[i][j] == 0:
                    dp[i][j] = (0, 0)
                else:
                    n11 = dp[i - 1][j][1] * grid[i][j] if dp[i - 1][j][1] is not None else None
                    n12 = dp[i][j - 1][1] * grid[i][j] if dp[i][j - 1][1] is not None else None
                    if n11 is not None and n12 is not None:
                        n1 = max(n11, n12)
                    elif n11 is not None:
                        n1 = n11
                    elif n12 is not None:
                        n1 = n12
                    else:
                        n1 = None

                    n21 = dp[i - 1][j][0] * grid[i][j] if dp[i - 1][j][0] is not None else None
                    n22 = dp[i][j - 1][0] * grid[i][j] if dp[i][j - 1][0] is not None else None
                    if n21 is not None and n22 is not None:
                        n2 = min(n21, n22)
                    elif n21 is not None:
                        n2 = n21
                    elif n22 is not None:
                        n2 = n22
                    else:
                        n2 = None
                    # print("(", i, ",", j, ")", grid[i][j], "->", n11, n12, n21, n22, "->", n1, n2)
                    dp[i][j] = (n1, n2)

        # for l in dp:
        #     print(l)

        if dp[-1][-1][0] is not None:
            return dp[-1][-1][0] % (10 ** 9 + 7)
        else:
            return -1
```