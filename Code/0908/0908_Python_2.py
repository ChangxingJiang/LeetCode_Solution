from typing import List


class Solution:
    def smallestRangeI(self, A: List[int], K: int) -> int:
        maximum = float("-inf")
        minimum = float("inf")
        for a in A:
            if a > maximum:
                maximum = a
            if a < minimum:
                minimum = a
        ans = maximum - minimum - 2 * K
        if ans > 0:
            return ans
        else:
            return 0


if __name__ == "__main__":
    print(Solution().smallestRangeI(A=[1], K=0))  # 0
    print(Solution().smallestRangeI(A=[0, 10], K=2))  # 6
    print(Solution().smallestRangeI(A=[1, 3, 6], K=3))  # 0
