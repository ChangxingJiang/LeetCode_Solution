from typing import List


class Solution:
    def lenLongestFibSubseq(self, A: List[int]) -> int:
        S = set(A)

        size = len(A)

        ans = 0

        for i in range(size):
            for j in range(i + 1, size):
                # 剪枝条件：A[i]+A[j]>A[-1]
                if A[i] + A[j] > A[-1]:
                    break
                n1, n2, n3 = A[i], A[j], A[i] + A[j]
                length = 2
                while n3 in S:
                    length += 1
                    n1, n2, n3 = n2, n3, n2 + n3

                if length >= 3:
                    ans = max(ans, length)

        return ans


if __name__ == "__main__":
    print(Solution().lenLongestFibSubseq([1, 2, 3, 4, 5, 6, 7, 8]))  # 5
    print(Solution().lenLongestFibSubseq([1, 3, 7, 11, 12, 14, 18]))  # 3
