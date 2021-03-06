from typing import List


class Solution:
    def arrayRankTransform(self, arr: List[int]) -> List[int]:
        hashmap = {}
        srr = list(set(arr))
        srr.sort()
        for i in range(len(srr)):
            hashmap[srr[i]] = i + 1
        return [hashmap[a] for a in arr]


if __name__ == "__main__":
    print(Solution().arrayRankTransform(arr=[40, 10, 20, 30]))  # [4,1,2,3]
    print(Solution().arrayRankTransform(arr=[100, 100, 100]))  # [1,1,1]
    print(Solution().arrayRankTransform(arr=[37, 12, 28, 9, 100, 56, 80, 5, 12]))  # [5,3,4,2,8,6,7,1,3]
