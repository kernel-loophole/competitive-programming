from tree import node
from tree import preorder
import numpy as np

# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def fac(n):
    if n == 0:
        return 1
    l = [1, 2, 3, 4]
    return n * fac(n - 1)


def inorder_test(root, res):
    # Recursive traversal

    if root:
        inorder(root.left, res)
        res.append(root.val)
        # print(root.val)
        inorder(root.right, res)
        return res


def test_tree(root, res):
    if root:

        if root.right:
            root_right = root.right
            root_left = root.right.right
            root = root_right
            x = inorder(root, [])
            print(x)
            res.append(x)
        print(root.val)

        test_tree(root.right, res)
        test_tree(root.left, res)
    return res


def make_insertion(root, num_list):
    current = True
    for i in num_list:
        if current:
            n = node(i)
            current = False
            continue
        n.insert(i)
    return n


def right_side(root, res):
    if root.right:
        right_side(root.right, res)
    res.append(root.val)
    if root.left:
        right_side(root.left, res)
    # print(res)
    return res


def left_side(root, res):
    if root.right:
        left_side(root.right, res)
    res.append(root.val)
    if root.left:
        left_side(root.left, res)
    # print(res)
    return res


def inorder(root, res):
    # Recursive traversal
    if root:
        inorder(root.right, res)
        res.append(root.val)
        print(root.val)
        inorder(root.left, res)
    return res


def inorder_(root, res):
    # Recursive traversal
    if root:
        # inorder(root.left, res)
        if root.right:
            # res.append(root.right.val)
            tmp_list = []
            x = right_side(root, tmp_list)
        # print(x)
        #           if root.left.val in res:
        #                pass
        #            else:
        #                res.append(root.left.val)
        inorder(root.right, res)
        if root.left:
            tmp_list = []
            y = right_side(root, tmp_list)
            # print(root.val)
        inorder(root.left, res)


class Solution:
    def generateTrees(self, n):
        """
        :type n: int        :rtype: List[TreeNode]
        """
        nu = fac(n)
        #    final_list=[]
        #    for i in range(1,nu):
        #        tmp_list=[]
        #        for j in range(1,n):
        #            tmp_list.append(j)

        #        # print(i)
        list_of_number = np.arange(1, n + 1)
        # print(list_of_number)
        n_fac = fac(n)
        for i in range(0, n_fac):
            current = False
            for j in list_of_number:
                if current == False:
                    new_node = node(j)
                    current = True
                    continue
                #        print("inserting ===>",j)
                new_node.insert(j)
            # tmp_list = inorder(new_node, [])
            # tmp_list_1 = preorder(new_node, [])

        x = test_tree(new_node, [])

        print(x)
        # print(tmp_list)
        #  print(tmp_list_1)
        # make_insertion(n, tmp_list_1)


if __name__ == "__main__":
    s = Solution()
    s.generateTrees(5)
#  n=node(10)
#  n.insert(9)
#  inorded(n,[])
#
