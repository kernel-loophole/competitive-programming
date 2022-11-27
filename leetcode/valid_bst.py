from tree import node
#testing function
def isValidBST_(root):
    if root:
        if root.right:
            if root.right.val<=root.val:
                return False
            tmp_root=root.right
            while tmp_root:
                if tmp_root.right:
                    if tmp_root.val<=root.val:
                        # print("test+====",root.val,tmp_root.val)
                        return False
                tmp_root=tmp_root.right
        if root.left:
            if  root.val <=root.left.val:
                return False
            tmp_root=root.left
            while tmp_root:
                if tmp_root.left:
                    if  root.val <=tmp_root.left.val:
                        return False
                tmp_root=tmp_root.left

        isValidBST_(root.right)
        isValidBST_(root.left)
    return True
class Solution(object):
    def isValidBST(self, root):
        if isValidBST_(root):
            print("True")

            return True
        print("False")
        return False
if __name__=="__main__":
    s=Solution()
    root=node(2)
    root.insert(1)
    root.insert(3)
    root.insert(6)
    root.insert(8)
    root.insert(10)
    s.isValidBST(root)
