from typing import List


class Solution:
    def allPathsSourceTarget(self, graph: List[List[int]]) -> List[List[int]]:
        pass


if __name__ == "__main__":
    # [[0,1,3],[0,2,3]]
    print(Solution().allPathsSourceTarget(graph=[[1, 2], [3], [3], []]))

    # [[0,4],[0,3,4],[0,1,3,4],[0,1,2,3,4],[0,1,4]]
    print(Solution().allPathsSourceTarget(graph=[[4, 3, 1], [3, 2, 4], [3], [4], []]))

    # [[0,1]]
    print(Solution().allPathsSourceTarget(graph=[[1], []]))

    # [[0,1,2,3],[0,2,3],[0,3]]
    print(Solution().allPathsSourceTarget(graph=[[1, 2, 3], [2], [3], []]))

    # [[0,1,2,3],[0,3]]
    print(Solution().allPathsSourceTarget(graph=[[1, 3], [2], [3], []]))
