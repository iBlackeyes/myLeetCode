#!/usr/bin/env python
# encoding: utf-8
# qinliang@meituan.com
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

#  Sort a linked list in O(n log n) time using constant space complexity.
#  要求在O(n*logn)时间复杂度 且常量空间复杂度实现
class Solution(object):
    def sortList(self, head):
        if not head or not head.next:    # 判断条件不可少
            return head
        middle = self.getMiddlePos(head)
        lHead = head
        rHead = middle.next
        middle.next = None
        return self.mergeNode(self.sortList(lHead), self.sortList(rHead))

    def getMiddlePos(self, head):
        if not head:        # 判断时间不可少
            return head
        fast = slow = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def mergeNode(self, lHead, rHead):
        dumNode = ListNode(0)
        dumHead = dumNode

        i, j = lHead, rHead
        while i and j:
            if i.val < j.val:
                dumNode.next = i
                i = i.next
            else:
                dumNode.next = j
                j = j.next
            dumNode = dumNode.next    # important
        if i:
            dumNode.next = i
        if j:
            dumNode.next = j

        return dumHead.next

if __name__ == "__main__":
    node1 = ListNode(2)
    node2 = ListNode(1)
    node3 = ListNode(3)
    head = node1
    node1.next = node2
    node2.next = node3
    solution = Solution()
    head = solution.sortList(head)
    while True:
        if not head:
            break
        print head.val
        head = head.next
