from toolkit import ListNode


class Solution:
    def deleteNode(self, head: ListNode, val: int) -> ListNode:
        pass


if __name__ == "__main__":
    print(Solution().deleteNode(ListNode([4, 5, 1, 9]), val=5))  # [4,1,9]
    print(Solution().deleteNode(ListNode([4, 5, 1, 9]), val=1))  # [4,5,9]
