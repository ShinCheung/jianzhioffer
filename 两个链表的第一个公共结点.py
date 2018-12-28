# -*- coding:utf-8 -*-

# 输入两个链表，找出它们的第一个公共结点。
# 重要：两条相交的链表呈Y型

# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# 有个思路，不需要存储链表的额外空间。也不需要提前知道链表的长度。看下面的链表例子：
# 0-1-2-3-4-5-null
# a-b-4-5-null
# 代码的ifelse语句，对于某个指针p1来说，其实就是让它跑了连接好的的链表，长度就变成一样了。
# 如果有公共结点，那么指针一起走到末尾的部分，也就一定会重叠。看看下面指针的路径吧。
# p1： 0-1-2-3-4-5-null(此时遇到ifelse)-a-b-4-5-null
# p2:  a-b-4-5-null(此时遇到ifelse)0-1-2-3-4-5-null
# 因此，两个指针所要遍历的链表就长度一样了！
class Solution:
    def FindFirstCommonNode(self, pHead1, pHead2):
        # write code here
        p1=pHead1
        p2=pHead2
        while p1 != p2:
            p1=p1.next if p1 != None else pHead2
            p2=p2.next if p2 != None else pHead1
        return p2

# 另两种思路
# 思路一：两条相交的链表呈Y型。可以从两条链表尾部同时出发，最后一个相同的结点就是链表的第一个相同的结点。
# 可以利用栈来实现。时间复杂度有O(m + n), 空间复杂度为O(m + n)
    def FindFirstCommonNode1(self, pHead1, pHead2):
        if not pHead1 or not pHead2:
            return None

        stack1 = []
        stack2 = []
        while pHead1:
            stack1.append(pHead1)
            pHead1 = pHead1.next    
        while pHead2:
            stack2.append(pHead2)
            pHead2 = pHead2.next
             
        first = None
        while stack1 and stack2:
            top1 = stack1.pop()
            top2 = stack2.pop()
            if top1 is top2:
                first = top1
            else:
                break
        return first
# 思路二：
# 思路一其实利用栈主要解决就是同时到达第一个结点的问题。那么从链表头出发如何同时到达第一个相同的结点呢? 
# 链表的长度相同就可以，其实就是走的结点数目相同。所以可以让其中长的链表先走几步，剩余的长度到短链表的长度相同。
def FindFirstCommonNode2(self, head1, head2):
        if not head1 or not head2:
            return None
 
        p1, p2= head1, head2
        length1 = length2 = 0
 
        while p1:
            length1 += 1
            p1 = p1.next
        while p2:
            length2 += 1
            p2 = p2.next
 
        if length1 > length2:
            while length1 - length2:
                head1 = head1.next
                length1 -= 1
        else:
            while length2 - length1:
                head2 = head2.next
                length2 -= 1
 
        while head1 and head2:
            if head1 is head2:
                return head1
            head1 = head1.next
            head2 = head2.next
 
        return None
