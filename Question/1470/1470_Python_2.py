from typing import List


class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        ans = []
        for i in range(n):
            ans.append(nums[i])
            ans.append(nums[n + i])
        return ans


if __name__ == "__main__":
    print(Solution().shuffle(nums=[2, 5, 1, 3, 4, 7], n=3))  # [2,3,5,4,1,7]
    print(Solution().shuffle(nums=[1, 2, 3, 4, 4, 3, 2, 1], n=4))  # [1,4,2,3,3,2,4,1]
    print(Solution().shuffle(nums=[1, 1, 2, 2], n=2))  # [1,2,1,2]
