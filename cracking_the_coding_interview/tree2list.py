# -*- coding:utf-8 -*-
'''
有一个类似结点的数据结构TreeNode，包含了val属性和指向其它结点的指针。
其可以用来表示二叉查找树(其中left指针表示左儿子，right指针表示右儿子)。
请编写一个方法，将二叉查找树转换为一个链表，其中二叉查找树的数据结构用TreeNode实现，链表的数据结构用ListNode实现。

给定二叉查找树的根结点指针root，请返回转换成的链表的头指针。
'''
class ListNode:
  def __init__(self, x):
    self.val = x
    self.next = None

class TreeNode:
  def __init__(self, x):
    self.val = x
    self.left = None
    self.right = None

class Converter:
  def treeToList(self, root):
    # write code here
    self.L = ListNode(0)
    self.List = self.L
    self.inOrderTraversal(root)
    return self.List.next

  def inOrderTraversal(self, root):
    if (root.left != None):
      self.inOrderTraversal(root.left)
    # inOrder
    self.L.next = ListNode(root.val)
    self.L = self.L.next
    print(root.val) # debug: for testing, delete when submit
    if (root.right != None):
      self.inOrderTraversal(root.right)

# testcase
T = TreeNode(1)
T.left = TreeNode(2)
T.right = TreeNode(3)
T.left.left = TreeNode(4)
T.left.right = TreeNode(5)
T.right.left = TreeNode(6)
T.right.right = TreeNode(7)
Converter().treeToList(T)