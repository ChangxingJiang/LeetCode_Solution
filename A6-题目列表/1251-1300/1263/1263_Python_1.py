from typing import List


class Solution:
    def minPushBox(self, grid: List[List[str]]) -> int:
        pass


if __name__ == "__main__":
    # 3
    print(Solution().minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
                                      ["#", "T", "#", "#", "#", "#"],
                                      ["#", ".", ".", "B", ".", "#"],
                                      ["#", ".", "#", "#", ".", "#"],
                                      ["#", ".", ".", ".", "S", "#"],
                                      ["#", "#", "#", "#", "#", "#"]]))

    # -1
    print(Solution().minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
                                      ["#", "T", "#", "#", "#", "#"],
                                      ["#", ".", ".", "B", ".", "#"],
                                      ["#", "#", "#", "#", ".", "#"],
                                      ["#", ".", ".", ".", "S", "#"],
                                      ["#", "#", "#", "#", "#", "#"]]))

    # 5
    print(Solution().minPushBox(grid=[["#", "#", "#", "#", "#", "#"],
                                      ["#", "T", ".", ".", "#", "#"],
                                      ["#", ".", "#", "B", ".", "#"],
                                      ["#", ".", ".", ".", ".", "#"],
                                      ["#", ".", ".", ".", "S", "#"],
                                      ["#", "#", "#", "#", "#", "#"]]))

    # -1
    print(Solution().minPushBox(grid=[["#", "#", "#", "#", "#", "#", "#"],
                                      ["#", "S", "#", ".", "B", "T", "#"],
                                      ["#", "#", "#", "#", "#", "#", "#"]]))
