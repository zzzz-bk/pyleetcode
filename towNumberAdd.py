# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution(object):
    def addTwoNumbers(self, l1:ListNode, l2:ListNode):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = ListNode()
        p = head
        add = False
        while True:
            if l1==None and l2==None and not add:
                break
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            p.val = v1 + v2 + add
            add = p.val >= 10
            p.val = p.val % 10 if p.val >= 10 else p.val
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
            if l1 or l2 or add:
                p.next = ListNode()
                p = p.next
        return head

if __name__ == '__main__':
    n1 = ListNode(2,ListNode(4,ListNode(3,ListNode(9))))
    n2 = ListNode(5,ListNode(6,ListNode(4)))
    s = Solution()
    head = s.addTwoNumbers(n1,n2)
    print(head.val)