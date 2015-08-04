__author__ = 'pisx'
import time
import random
import sys


# 插入排序
def insertion_sort(a):
    if len(a) == 1:
        return
    for cursor in range(1, len(a)):
        i = cursor - 1
        t = a[cursor]
        while i >= 0 and t < a[i]:
            a[i + 1] = a[i]
            i -= 1
        a[i + 1] = t
    return


# 递归形势插入排序 经过简单测试比迭代的速度快
# 缺点是大数据递归调用过多 会导致递归方法栈过大  可以理解为用空间换了时间
def insertion_sort2(n):
    if len(n) == 1:
        return n
    b = insertion_sort2(n[1:])
    m = len(b)
    for i in range(m):
        if n[0] <= b[i]:
            return b[:i] + [n[0]] + b[i:]
    return b + [n[0]]


# shell sort
# 希尔排序通过将比较的全部元素分为几个区域来提升插入排序的性能。
# 这样可以让一个元素可以一次性地朝最终位置前进一大步。
# 然后算法再取越来越小的步长进行排序，算法的最后一步就是普通的插入排序，
# 但是到了这步，需排序的数据几乎是已排好的了（此时插入排序较快）。
def shell_sort(a):
    h = 1
    while h <= len(a):
        h = h * 3 + 1  # <O(n^(3/2)) by Knuth,1973>: 1, 4, 13, 40, 121, ...
    while h > 0:

        for c in range(h, len(a)):
            t = a[c]
            i = c - h
            while i >= 0 and a[i] > t:
                a[i + h] = a[i]
                i -= h
            a[i + h] = t

        h = int((h - 1) / 3)
    return


# Selection sort
def selection_sort(a):
    a_len = len(a)
    for i in range(a_len - 1):
        cur_min_p = i  # 记录此次遍历最小数的位置
        # 从后面部分查找最小数
        for j in range(i + 1, a_len):
            if a[cur_min_p] > a[j]:
                cur_min_p = j
        if cur_min_p != i:
            tmp = a[cur_min_p]
            a[cur_min_p] = a[i]
            a[i] = tmp
    return


# heap sort
def heap_sort(lst):
    def sift_down(start, end):
        """最大堆调整"""
        root = start
        while True:
            child = 2 * root + 1
            if child > end:
                break
            if child + 1 <= end and lst[child] < lst[child + 1]:
                child += 1
            if lst[root] < lst[child]:
                lst[root], lst[child] = lst[child], lst[root]
                root = child
            else:
                break

    # 创建最大堆
    for start in range(int((len(lst) - 2) / 2), -1, -1):
        sift_down(start, len(lst) - 1)

    # 堆排序
    for end in range(len(lst) - 1, 0, -1):
        lst[0], lst[end] = lst[end], lst[0]
        sift_down(0, end - 1)
    return


# Merge sort
def merge_sort(a):
    if len(a) <= 1:
        return a

    def merge(l, r):
        merged = []
        while l and r:
            merged.append(l.pop(0) if l[0] <= r[0] else r.pop(0))
        while l:
            merged.append(l.pop(0))
        while r:
            merged.append(r.pop(0))
        return merged

    mid = int(len(a) / 2)
    return merge(merge_sort(a[:mid]), merge_sort(a[mid:]))


def quick_sort(a):
    if len(a) <= 1:
        return a
    else:
        pivot = a[0]
        return quick_sort([x for x in a[1:] if x < pivot]) + [pivot] \
               + quick_sort([x for x in a[1:] if x >= pivot])


# 这个修改递归调用栈的最大深度
# Set the maximum depth of the Python interpreter stack to limit
# https://docs.python.org/2/library/sys.html#sys.setrecursionlimit
sys.setrecursionlimit(6000)

size = 100000
lst = []
for i in range(1, size):
    # lst.append(random.randrange(1,size))
    lst.append(i)
random.shuffle(lst)
print(lst)
start = time.time()
# insertion_sort(lst)
# shell_sort(lst)

# selection_sort(lst)
heap_sort(lst)
# merged = merge_sort(lst)
# print(merged)
# ra = quick_sort(lst)
# print(ra)
print(lst)
print(time.time() - start)
