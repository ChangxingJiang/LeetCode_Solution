from typing import List


class Solution:
    def printNumbers(self, n: int) -> List[int]:
        return [i for i in range(1, 10 ** n)]


if __name__ == "__main__":
    #  [1,2,3,4,5,6,7,8,9]
    print(Solution().printNumbers(1))
