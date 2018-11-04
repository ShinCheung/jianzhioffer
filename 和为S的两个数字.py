# -*- coding:utf-8 -*-

# 输入一个递增排序的数组和一个数字S，在数组中查找两个数，使得他们的和正好是S
# 如果有多对数字的和等于S，输出两个数的乘积最小的

class Solution:
    def FindNumbersWithSum(self, array, tsum):
        # write code here
        l=[]
        for x in array:
            l.append(tsum-x)
        for y in l:
            if y in array:
                return [tsum-y,y]
        return []