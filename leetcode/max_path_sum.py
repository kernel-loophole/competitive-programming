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
                else:
                    self.left.insert(val)
            elif val > self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
            elif val== self.val:
                if self.right is None:
                    self.right = node(val)
                else:
                    self.right.insert(val)
        else:
            self.val = val
list_no=[]
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        sum=0
        x=final_fn(root,sum)
        print(x)
        return max(x)

def final_fn(root,count):
    if root:
        
        if root.right:
           x= add_to(root.right,count+root.right.val)
           list_no.append(x+root.val)
           final_fn(root.right,count)
        
        if root.left:
            y=add_to(root.left,count+root.left.val)
            
            list_no.append(y+root.val)
            final_fn(root.left,count)
    return list_no



def add_to(root,sum_no):
    if root:
        
        if root.right:
            return add_to(root.right,sum_no+root.right.val)
        
        if root.left:
            return add_to(root.left,sum_no+root.left.val)
    return sum_no        
n=node(-10)
n.insert(9)
n.insert(20)
n.insert(15)
n.insert(7)
# inorder(n,[])
s=Solution()
print(s.maxPathSum(n))
# print(final_fn(n,0))
# print(list_no)
# if __name__=="__main__":
#     type_hint(12)