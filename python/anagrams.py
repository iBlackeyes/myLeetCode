#!/usr/bin/env python
# encoding: utf-8
# qinliang@meituan.com

class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        s = sorted(s)
        t = sorted(t)
        if s == t:
            return True
        else:
            return False

if __name__ == '__main__':
    s = "anaconda"
    t = "naaconda"
    solution = Solution()
    print solution.isAnagram(s, t)
