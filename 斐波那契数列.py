# -*- coding:utf-8 -*-

# 大家都知道斐波那契数列，现在要求输入一个整数n，请你输出斐波那契数列的第n项（从0开始，第0项为0）。

class Solution:
    def Fibonacci(self, n):
        # write code here
        a = [0,1,1]
        if n < 3:
            return a[n]
        for i in range(3,n+1):
            a.append(a[i-1] + a[i-2])
        return a[n]

print(Solution().Fibonacci(4))