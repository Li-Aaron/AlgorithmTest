'''
编写代码，以给定值x为基准将链表分割成两部分，所有小于x的结点排在大于或等于x的结点之前

给定一个链表的头指针 ListNode* pHead，请返回重新排列后的链表的头指针。注意：分割以后保持原来的数据顺序不变。
'''
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class Partition:
  def partition(self, pHead, x):
    pSmallHead = ListNode(0)
    pLargeHead = ListNode(0)
    pSmall = pSmallHead
    pLarge = pLargeHead
    while pHead != None:
      if pHead.val < x:
        pSmall.next = pHead
        pSmall = pSmall.next
      else:
        pLarge.next = pHead
        pLarge = pLarge.next
      pHead = pHead.next
    pLarge.next = None
    pSmall.next = pLargeHead.next
    return pSmallHead.next

