#!/usr/bin/env python
# encoding: utf-8
# qinliang@meituan.com
class Solution(object):
    def sortList(self, head):
        if not head:
            return head
        res = head
        while res:
            while True:
                if not head.next.next:
                    break
                cur_node = head.next.next
                if cur_node.val < head.next.val:
                    head.next, cur = head.



if __name__ == '__main__' :
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


