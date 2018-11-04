# -*- coding:utf-8 -*-

# 找出所有和为S的连续正数序列

class Solution:
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum < 3:
            return []
        small=1
        big=2
        middle = (1+tsum)/2
        curSum = small+big
        output=[]
        while small < middle:
            if curSum == tsum:
                output.append(range(small,big+1))
                big += 1
                curSum += big
            elif curSum >= tsum:
                curSum -= small
                small += 1
            else:
                big += 1
                curSum += big
        return output