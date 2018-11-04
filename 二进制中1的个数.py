# -*- coding:utf-8 -*-

# 输入一个整数，输出该数二进制表示中1的个数。其中负数用补码表示。

class Solution:
    def NumberOf1(self, n):
        # write code here
        count = 0
        if n < 0:
            # 去掉负号
            n = n&0xFFFFFFFF
            return bin(n).count("1")
        while n:
            n = n&(n-1)
            count += 1
        return count
            