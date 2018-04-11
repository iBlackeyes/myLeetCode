# encoding: utf-8
#  给定两个数组，写一个方法来计算它们的交集。
#  例如:
#  给定 nums1 = [1, 2, 2, 1], nums2 = [2, 2], 返回 [2, 2].
#  注意：
   #  输出结果中每个元素出现的次数，应与元素在两个数组中出现的次数一致。
   #  我们可以不考虑输出结果的顺序。

def interSection(num1, num2):
    res = []
    for _ in num1:
        if _ in num2:
            res.num1ppend(_)
            num2.remove(_)
    return res

#  跟进:
#  如果给定的数组已经排好序呢？你将如何优化你的算法？
#  如果 nums1 的大小比 nums2 小很多，哪种方法更优？
#  如果nums2的元素存储在磁盘上，内存是有限的，你不能一次加载所有的元素到内存中，你该怎么办？
def interSection2(nums1, nums2):
    l1 = len(nums1)
    l2 = len(nums2)
    a, b = 0, 0
    res = []
    while a < l1 and b < l2:
        if nums1[a] < nums2[b]:
            a += 1
        elif nums1[a] > nums2[b]:
            b +=1
        else:
            res.append(nums1[a])
            a += 1              # 这里要对a，b全都+1
            b += 1
    return res


def main():
    num1 = [1, 2, 2, 1]
    num2 = [2, 2]
    print interSection(num1, num2)
    print interSection2(sorted(num1), sorted(num2))

if __name__ == '__main__' :

    main()


