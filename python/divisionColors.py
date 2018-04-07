#!/usr/bin/env python
# encoding: utf-8
#  给定一个包含红色、白色和蓝色，且含有 n 个元素的数组，对它们进行排序，使得相同颜色的元素相邻，颜色顺序为红色、白色、蓝色。
#  此题中，我们使用整数 0, 1 和 2 分别表示红色，白色和蓝色。
#  注意:
#  不能使用代码库中的排序函数来解决这道题。

def solution(nums):
    res = []
    m = 0
    for _ in nums:
        if _ == 0:
            res.insert(0, _)
            m += 1
        elif _ == 1:
            res.insert(m, _)
        else:
            res.append(_)

    return res

#  原址排序
def solution2(nums):
    n2 = 0
    n0 = 0
    for i, _ in enumerate(nums):
        if _ == 0: n0 += 1
        if _ == 2: n2 += 1
        nums[i] = 1
    print nums
    if n0:
        nums[:n0] = [0] * n0
    if n2:
        nums[-n2:] = [2] * n2           # 切记是 -n2
    print n0, n2

# 还有一种方法： 不同的值 增加的步长不一样

if __name__ == '__main__' :
    nums = [0,2,2,1,0,2,1,1,2,0]
    print nums
    print solution(nums)
    solution2(nums)
    print nums


