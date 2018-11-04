# -*- coding:utf-8 -*-

# 例如:{6,-3,-2,7,-15,1,2,2},连续子向量的最大和为8(从第0个开始,到第3个为止)

class Solution:
    def FindGreatestSumOfSubArray(self, array):
        # write code here
        for i in range(1,len(array)):
            if array[i-1] > 0:
                array[i] += array[i-1]
        return max(array)