from typing import List


class Solution:
    def fairCandySwap(self, A: List[int], B: List[int]) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().fairCandySwap(A=[1, 1], B=[2, 2]))  # [1,2]
    print(Solution().fairCandySwap(A=[1, 2], B=[2, 3]))  # [1,2]
    print(Solution().fairCandySwap(A=[2], B=[1, 3]))  # [2,3]
    print(Solution().fairCandySwap(A=[1, 2, 5], B=[2, 4]))  # [5,4]
