from typing import List

from toolkit import TreeNode, build_TreeNode


class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        pass


if __name__ == "__main__":
    print(Solution().postorderTraversal(build_TreeNode([1, None, 2, 3])))  # [3,2,1]
