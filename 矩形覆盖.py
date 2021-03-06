# -*- coding:utf-8 -*-

# 我们可以用2*1的小矩形横着或者竖着去覆盖更大的矩形。请问用n个2*1的小矩形无重叠地覆盖一个2*n的大矩形，总共有多少种方法？

class Solution:
    def rectCover(self, number):
        # write code here
        if number < 1:
            return 0
        if number == 1 or number == 2:
            return number
        a,b = 1,1
        while number > 1:
            a,b = b,a+b
            number -= 1
        return b