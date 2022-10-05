from tree import node
from tree import inorder
from tree import preorder
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge():
        print()
if __name__=="__main__":
    node_list=[[5,3,8],[3,2,6]]
    counter=0
    for i in node_list:
        if counter==0:
            node_=node(i[0])
        for j in i:
            node_.insert(j)
        counter+=1
    res = []
    inorder(node_,res)
    preorder(node_)
