# -*- coding:utf-8 -*-

# 正确的句子应该是“I am a student.”
# “student. a am I”

class Solution:
    def ReverseSentence(self, s):
        # write code here
        return " ".join(s.split(" ")[::-1])