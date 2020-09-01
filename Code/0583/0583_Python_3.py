class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        # 生成状态表格
        N1, N2 = len(word1), len(word2)
        matrix = [0] * (N1 + 1)

        # 状态计算
        for i in range(1, N2 + 1):
            last = 0
            for j in range(1, N1 + 1):
                tmp = matrix[j]
                if word2[i - 1] == word1[j - 1]:
                    matrix[j] = last + 1
                else:
                    matrix[j] = max(matrix[j], matrix[j - 1])
                last = tmp

        # 生成结果
        return N1 + N2 - 2 * matrix[-1]


if __name__ == "__main__":
    print(Solution().minDistance("sea", "eat"))  # 2
    print(Solution().minDistance("", ""))  # 0
    print(Solution().minDistance("se", ""))  # 2
    print(Solution().minDistance("a", "a"))  # 0
    print(Solution().minDistance("park", "spake"))  # 3
    print(Solution().minDistance("horse", "ros"))  # 4
    print(Solution().minDistance("dinitrophenylhydrazine", "dimethylhydrazine"))  # 9
    print(Solution().minDistance("intention", "execution"))  # 8
