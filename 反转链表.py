# -*- coding:utf-8 -*-

# 输入一个链表，反转链表后，输出新链表的表头。
# 思路:新建一个头结点，遍历原链表，把每个节点用头结点插入到新建链表中。最后，新建的链表就是反转后的链表。
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None
class Solution:
    # 返回ListNode
    def ReverseList(self, pHead):
        # write code here
        if pHead==None or pHead.next==None:
            return pHead
        last = None
        # pHead是要插入到新链表的节点
        # tmp是临时保存的pHead的next
        while pHead:
            tmp = pHead.next    # tmp保存下一次要插入的节点
            pHead.next = last   # 把pHead插入到last中
            last = pHead        # 纠正头结点last的指向
            pHead = tmp         # pHead指向下一次要插入的节点
        return last
