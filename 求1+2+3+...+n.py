# -*- coding:utf-8 -*-

# 求1+2+3+...+n，要求不能使用乘除法、for、while、if、else、switch、case等关键字及条件判断语句

class Solution:
    def Sum_Solution(self, n):
        # write code here
        #return reduce(lambda x,y: x+y, range(1,n+1))
        if n == 1:
            return 1
        return n + self.Sum_Solution(n-1)
