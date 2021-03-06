# LeetCode题解(1290)：二进制链表转换为整数(Python)

题目：[原题链接](https://leetcode-cn.com/problems/convert-binary-number-in-a-linked-list-to-integer/)（简单）

标签：链表

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 40ms (73.32%) |
| Ans 2 (Python) | $O(N)$     | $O(1)$     | 40ms (73.32%) |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（位运算）：

```python
def getDecimalValue(self, head: ListNode) -> int:
    ans = 0
    while head:
        ans = ans << 1
        ans = ans ^ head.val
        head = head.next
    return ans
```

解法二：

```python
def getDecimalValue(self, head: ListNode) -> int:
    ans = 0
    while head:
        ans *= 2
        ans += head.val
        head = head.next
    return ans
```