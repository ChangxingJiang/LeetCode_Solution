from typing import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        pass


if __name__ == "__main__":
    print(Solution().evalRPN(["2", "1", "+", "3", "*"]))  # 9
    print(Solution().evalRPN(["4", "13", "5", "/", "+"]))  # 6
    print(Solution().evalRPN(["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"]))  # 22
