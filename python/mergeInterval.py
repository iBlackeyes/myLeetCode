#!/usr/bin/env python
# encoding: utf-8
# qinliang@meituan.com

#  给出一个区间的集合, 请合并所有重叠的区间。
#  示例：
#  给出 [1,3],[2,6],[8,10],[15,18],
#  返回 [1,6],[8,10],[15,18].
### 时间超时
def merge(intervals):
    res = []
    intervals = sorted(intervals, key=lambda _: _[0])
    res.append(intervals[0])
    l = len(intervals)
    for _ in intervals[1:]:
        print _
        if _[0] > res[-1][-1]:
            res.append(_)
        elif _[-1] > res[-1][-1]:
            res[-1][-1] = _[-1]
    return res

def bubble_sort(lists):
    l = len(lists)
    for m in range(l - 2):
        for n in range(m + 1, l - 1):
            if lists[m]


if __name__ == '__main__' :
    intervals = [[1, 3], [2, 6], [8, 10], [15, 18]]
    print merge(intervals)


