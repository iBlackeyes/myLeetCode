#!/usr/bin/env python
# encoding: utf-8
# qinliang@meituan.com

#  给出一个区间的集合, 请合并所有重叠的区间。
#  示例：
#  给出 [1,3],[2,6],[8,10],[15,18],
#  返回 [1,6],[8,10],[15,18].
### 时间超时
class Interval(object):
    def __init__(self, s, t):
        self.start = s
        self.end = t

def merge(intervals):
    res = []
    if len(intervals) <= 1:
        return intervals

    intervals = sorted(intervals, key=lambda _: _.start)
    res.append(intervals[0])
    l = len(intervals)
    for _ in intervals[1:]:
        if _.start > res[-1].end:
            res.append(_)
        elif _.end > res[-1].end:
            res[-1].end = _.end
    for _ in res:
        print _.start, _.end
    return res

### 方法2：对starts，ends分别排序，判断后取区间
def merge2(intervals):
    res = []
    if len(intervals) <= 1:
        return intervals
    starts = sorted(map(lambda _: _.start, intervals))
    ends = sorted(map(lambda _: _.end, intervals))
    j = 0
    l = len(starts)
    for i in range(l):
        if i == l-1 or starts[i+1] > ends[i]:
            res.append(Interval(starts[j], ends[i]))
            j = i + 1
    for _ in res:
        print _.start, _.end
    return res


if __name__ == '__main__' :
    intervals = [Interval(1, 3), Interval(2, 6), Interval(8, 10), Interval(15, 18)]
    #  print merge(intervals)
    print merge2(intervals)


