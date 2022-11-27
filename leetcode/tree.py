"""
the main module for tree
>>>tree insertion
"""


class node:
    # BST data structure
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

    def insert(self, val):
        if self.val:

            if val < self.val:
                if self.left is None:
                    self.left = node(val)
                    # self.left.right=None
                    # self.left.left=None
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                    # self.right.left=None
                    # self.right.right=None
                else:
                    self.right.insert(val)


#    if node
#     return
#
# # Otherwise
# if key < no
#     node.le
# else:
#     node.ri
#
# # return th
# return node
#
# #
#
#
#
#
#
# return th
# return node

#        if self.val:
#            if val < self.val:
#                if self.left is None:
#                    self.left = node(val)
#                else:
#                    self.left.insert(val)
#            elif val > self.val:
#                if self.right is None:
#                    self.right = node(val)
#                else:
#                    self.right.insert(val)
#            elif val== self.val:
#                if self.right is None:
#                    self.right = node(val)
#                else:
#                    self.right.insert(val)
#        else:
#            self.val = val


def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.left, res)
        res.append(root.val)
        # print(root.val)
        inorder(root.right, res)
    return res


def preorder(root, res_list):
    if root.right:
        preorder(root.right, res_list)
    res_list.append(root.val)
    if root.left:
        preorder(root.left, res_list)
    return res_list


def tree_sort(arr):
    # Build BST
    if len(arr) == 0:
        return arr
    root = node(arr[0])
    for i in range(1, len(arr)):
        root.insert(arr[i])
    # Traverse BST in order.
    res = []
    inorder(root, res)
    return res
