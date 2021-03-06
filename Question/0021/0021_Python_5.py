from toolkit import ListNode


class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        ans = node = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                node.next = ListNode(l1.val)
                l1 = l1.next
            else:
                node.next = ListNode(l2.val)
                l2 = l2.next
            node = node.next
        if l1 or l2:
            node.next = l1 or l2
        return ans.next


if __name__ == "__main__":
    print(Solution().mergeTwoLists(ListNode([1, 2, 4]), ListNode([1, 3, 4])))
    print(Solution().mergeTwoLists(ListNode([2]), ListNode([1])))
