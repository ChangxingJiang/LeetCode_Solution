# LeetCode题解(0595)：查找符合标准的记录(SQL)

题目：[原题链接](https://leetcode-cn.com/problems/big-countries/)（简单）

| 解法        | 执行用时       |
| ----------- | -------------- |
| Ans 1 (SQL) | 205ms (54.82%) |

>  LeetCode的Python执行用时随缘，只要时间复杂度没有明显差异，执行用时一般都在同一个量级，仅作参考意义。

解法一：

```sql
SELECT name, population, area
FROM World
WHERE area > 3000000
  OR population > 25000000;
```