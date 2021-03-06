# LeetCode题解(0876)：链表的中间结点(Python)

题目：[原题链接](https://leetcode-cn.com/problems/middle-of-the-linked-list/)（简单）

标签：链表、链表-双指针、链表-快慢针

| 解法           | 时间复杂度 | 空间复杂度 | 执行用时      |
| -------------- | ---------- | ---------- | ------------- |
| Ans 1 (Python) | $O(N)$     | $O(1)$     | 36ms (80.37%) |
| Ans 2 (Python) |            |            |               |
| Ans 3 (Python) |            |            |               |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一（快慢针）：

```python
def middleNode(self, head: ListNode) -> ListNode:
    fast = slow = head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow
```

