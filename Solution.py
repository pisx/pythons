class Solution:
    # @param s, a string
    # @return an integer
    def lengthOfLastWord(self, s):
        s = s.rstrip()
        c = 0
        s_len = len(s)
        if s_len > 0:
            for i in range(s_len):
                l = s_len - i - 1
                if s[l] != ' ':
                    c += 1
                else:
                    break
        return c

    def lengthOfLastWord2(self, s):
        c = 0
        if s:
            cursor = len(s) - 1
            while cursor >= 0 and s[cursor] == ' ':
                cursor -= 1

            while cursor >= 0 and s[cursor] != ' ':
                cursor -= 1
                c += 1
        return c

    # @return a string
    def convert(self, s, nRows):
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
