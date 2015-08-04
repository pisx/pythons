__author__ = 'pisx'


def convert(s, nRows):
    if nRows == 1:
        return s
    s_len = len(s)
    r = ''
    # 步进
    borderRowStep = 2 * nRows - 2
    # 0 to nRows-1
    for cursor in range(nRows):
        t = cursor
        if cursor == 0 or cursor == nRows - 1:
            # 头行和末行 步进不变 都为 2*nRows - 2
            while t < s_len:
                r += s[t]
                t += borderRowStep
        else:
            flag = True
            insideRowLargerStep = 2 * (nRows - cursor - 1)
            # 原步进 中插入 2步 步进
            insideRowSmallerStep = borderRowStep - insideRowLargerStep
            while t < s_len:
                r += s[t]
                if flag:
                    t += insideRowLargerStep
                else:
                    t += insideRowSmallerStep
                flag = not flag

    return r


# a = 'ABCD'
# r = convert(a, 2)
# print(r)

# Python提供了ord()函数获取字符的整数表示，chr()函数把编码转换为对应的字符
ord('A')
ord('中')
