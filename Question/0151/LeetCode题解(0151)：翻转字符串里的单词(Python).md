# LeetCode题解(0151)：翻转字符串里的单词(Python)

题目：[原题链接](https://leetcode-cn.com/problems/reverse-words-in-a-string/)（中等）

标签：字符串

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(N)$     | 40ms (77.98%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（Pythonic）：

```python
class Solution:
    def reverseWords(self, s: str) -> str:
        return " ".join(s.lstrip().split()[::-1])
```