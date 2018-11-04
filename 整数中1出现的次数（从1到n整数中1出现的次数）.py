# -*- coding:utf-8 -*-

# 求出任意非负整数区间中1出现的次数
# 1~13的整数中1出现的次数,包含1的数字有1、10、11、12、13因此共出现6次

class Solution:
    def NumberOf1Between1AndN_Solution(self, n):
        # write code here
        if n < 1:
            return 0
        # map的一个特色功能，类型转换，如下将int转为str
        a=map(str,range(n+1))
        ones=[i for i in a if '1' in i]
        return "".join(ones).count('1')