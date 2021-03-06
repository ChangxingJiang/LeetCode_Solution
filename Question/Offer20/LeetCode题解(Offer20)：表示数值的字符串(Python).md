# LeetCode题解(Offer20)：识别表示数值的字符串(支持正负号、E）(Python)

题目：[原题链接](https://leetcode-cn.com/problems/biao-shi-shu-zhi-de-zi-fu-chuan-lcof/)（中等）

标签：字符串、正则表达式、自动机、自动机-有限状态自动机

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | --         | --         | 44ms (77.81%) |
| Ans 2 (Python) | --         | --         | 48ms (55.80%) |
| Ans 3 (Python) | $O(N)$     | $O(N)$     | 60ms (9.84%)  |

解法一（正则表达式）：

```python
class Solution:
    def isNumber(self, s: str) -> bool:
        return re.match(r"^ *[-+]?(\d+\.?\d*|\.\d+)([Ee][-+]?\d+|) *$", s) is not None
```

解法二（捣蛋取巧法）：

```python
def isNumber(self, s: str) -> bool:
    try:
        float(s)
        return True
    except:
        return False
```

解法三（有效状态自动机）：

```python
class Automaton:
    def __init__(self):
        self.stat = 0
        self.table = {
            -1: [-1, -1, -1, -1, -1],  # 已确定无效的状态
            0: [0, 1, 3, 2, -1],  # 初始状态，尚无符号、小数点和有效数字
            1: [-1, -1, 3, 2, -1],  # 已有符号，尚无小数点、有效数字
            2: [-1, -1, 4, -1, -1],  # 已有符号、小数点，尚无有效数字
            3: [8, -1, 3, 4, 5],  # 已有符号、有效数字，尚无小数部分
            4: [8, -1, 4, -1, 5],  # 已有符号、有效数字和小数部分
            5: [-1, 6, 7, -1, -1],  # 已有e，尚无e后的符号和有效数字
            6: [-1, -1, 7, -1, -1],  # 已有e和e后的符号，尚无e后的有效数字
            7: [8, -1, 7, -1, -1],  # 已有e和e后的符号、有效数字
            8: [8, -1, -1, -1, -1],  # 已结束匹配数字部分
        }
        self.final = [False, False, False, False, True, True, False, False, True, True]  # [-1,8]

    def get(self, ch: str):
        # 计算当前状态
        if ch.isspace():
            self.stat = self.table[self.stat][0]
        elif ch == "+" or ch == "-":
            self.stat = self.table[self.stat][1]
        elif ch.isdigit():
            self.stat = self.table[self.stat][2]
        elif ch == ".":
            self.stat = self.table[self.stat][3]
        elif ch == "e" or ch == "E":
            self.stat = self.table[self.stat][4]
        else:
            self.stat = -1

    def end(self):
        return self.final[self.stat + 1]


class Solution:
    def isNumber(self, s: str) -> bool:
        automaton = Automaton()
        for ch in s:
            automaton.get(ch)
        # print(s, ":", automaton.stat)
        return automaton.end()
```

