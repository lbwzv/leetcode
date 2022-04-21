# 两数相加：给你两个 非空 的链表，表示两个非负的整数。它们每位数字都是按照 逆序 的方式存储的，并且每个节点只能存储 一位 数字。

请你将两个数相加，并以相同形式返回一个表示和的链表。

方法一：递归
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
	if l1 is None:
	    return l2
	if l2 is None:
	    return l1
	x = l1.val if l1 else 0
	y = l2.val if l2 else 0
	re = ListNode((x + y) % 10)
	re.next = self.addTwoNumbers(l1.next, l2.next)
	if x + y > 9:
	    re.next = self.addTwoNumbers(re.next, ListNode((x + y) // 10))
	return re

方法二：循环
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        result = ListNode(0)
        re = result
        carry = 0
        # l1,l2,进位 有一个存在则需要继续链表
        while l1 or l2 or carry > 0:
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            re.next = ListNode((x + y + carry) % 10)
            re = re.next
            # 进位
            carry = (x + y + carry) // 10
            if l1 is not None:
                l1 = l1.next
            if l2 is not None:
               l2 = l2.next
        return result.next


