# -*- coding:utf-8 -*-

# 把只包含质因子2、3和5的数称作丑数（Ugly Number）。
# 例如6、8都是丑数，但14不是，因为它包含质因子7。 习惯上我们把1当做是第一个丑数。
# 求按从小到大的顺序的第N个丑数。

class Solution:
    def GetUglyNumber_Solution(self, index):
        # write code here
        if index <= 0:
            return 0
        uglyList = [1]
        index2,index3,index5 = 0,0,0
        for _ in range(index-1):
            newUgly = min(uglyList[index2]*2, uglyList[index3]*3, uglyList[index5]*5)
            uglyList.append(newUgly)
            if newUgly % 2 == 0:
                index2 += 1
            if newUgly % 3 == 0:
                index3 += 1
            if newUgly % 5 == 0:
                index5 += 1
        return uglyList[-1]