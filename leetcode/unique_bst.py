from tree import node
from tree import inorder
from tree import preorder
import numpy as np
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def fac(n):
    if n==0:
        return 1
    return n*fac(n-1)
def make_insertion(root,num_list):
    pass

class Solution():
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """
        nu=fac(n)
    #    final_list=[]
    #    for i in range(1,nu):
    #        tmp_list=[]
    #        for j in range(1,n):
    #            tmp_list.append(j)

    #        # print(i)
        list_of_number=np.arange(1,n+1)
        print(list_of_number)
        n_fac=fac(n)
        for i in  range(0,n_fac):
            current=False
            for j in list_of_number:
                if current ==False:
                    new_node=node(j)
                    current=True
                    continue 
                print("inserting ===>",j)
                new_node.insert(j)
            tmp_list=inorder(new_node,[])
            tmp_list_1=preorder(new_node,[])
            print(tmp_list)
            print(tmp_list_1)
        

if __name__=="__main__":
    s=Solution()
    s.generateTrees(3)
  #  n=node(10)
  #  n.insert(9)
  #  inorded(n,[])
  #      








