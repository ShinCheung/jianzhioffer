# -*- coding:utf-8 -*-

# 如果牌能组成顺子就输出true，否则就输出false。
# 为了方便起见,可以认为大小王是0,王可以看成任何数字,并且A看作1,J为11,Q为12,K为13
# 此题的思路是做差，差值之和最大为4，故n<=4即可

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if not numbers:
            return numbers
        new_list = [i for i in numbers if i > 0]
        new_list.sort()
        if len(new_list)==1:
            return True
        n = 0
        for j in range(len(new_list)-1):
            if (new_list[j+1] - new_list[j]) > 0:
                n += (new_list[j+1] - new_list[j])
            else:
                return False
        if n <= 4:
            return True
        else:
            return False