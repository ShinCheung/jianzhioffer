# -*- coding:utf-8 -*-

# 给定一个double类型的浮点数base和int类型的整数exponent。求base的exponent次方。

class Solution:
    def Power(self, base, exponent):
        # write code here
        if base == 0 or base == 1 or exponent == 1:
            return base
        elif exponent == 0:
            return 1
        else:
            return pow(base,exponent)