from typing import List


class Solution:
    def splitIntoFibonacci(self, S: str) -> List[int]:
        N = len(S)

        # 判断数字是否合法
        def is_valid(n):
            return not (int(n) > 0 and n[0] == "0") and int(n) <= (2 ** 31 - 1)

        # 检查是否为斐波那契数列
        def is_fibonacci(m, n):
            if not is_valid(S[:m]) or not is_valid(S[m:n]):
                return False
            lst = [int(S[:m]), int(S[m:n])]
            idx1 = n
            while idx1 < N:
                nn = lst[-1] + lst[-2]  # 当前项
                s1 = str(nn)
                idx2 = idx1 + len(s1)
                s2 = S[idx1:idx2]
                if is_valid(s2) and s1 == s2:
                    lst.append(nn)
                    idx1 = idx2
                else:
                    return False
            return lst

        # 筛选所有的斐波那契数列
        for i in range(1, N):
            for j in range(i + 1, N):
                fibonacci_lst = is_fibonacci(i, j)
                if fibonacci_lst:
                    return fibonacci_lst
        return []


if __name__ == "__main__":
    print(Solution().splitIntoFibonacci("123456579"))  # [123,456,579]
    print(Solution().splitIntoFibonacci("11235813"))  # [1,1,2,3,5,8,13]
    print(Solution().splitIntoFibonacci("112358130"))  # []
    print(Solution().splitIntoFibonacci("0123"))  # []
    print(Solution().splitIntoFibonacci("1101111"))  # [110, 1, 111] 或 [11,0,11,11]
    print(Solution().splitIntoFibonacci("17522"))  # [17,5,22]
