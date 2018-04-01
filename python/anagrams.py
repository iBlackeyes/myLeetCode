#!/usr/bin/env python
# encoding: utf-8
# qinliang@meituan.com
### method1: 对两个string排序，若排序结果一致，则说明两个string是anagrams
###         复杂度：
class Solution(object):
    def isAnagram(self, s, t):
        """tes"""
        if s == t:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "anaconda"
    t = "naaconda"
    solution = Solution()
    print solution.isAnagram(s, t)
