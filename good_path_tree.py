from tree import node
from tree import inorder
def check_val(root,counter,value):
    if root:
        if root.right:
            if root.right.val>value:
                # print(root.right.val)
                counter+=1
                # print(counter)
        if root.left:
            if root.left.val>value:
                # print(root.left.val)
                counter+=1
               
    if root:
        if root.right:
            return check_val(root.right,counter+1,value)
    if root:
        if root.left:
            return check_val(root.left,counter+1,value)
    else:
        return counter




def good_path(root,counter):
    # x=0
    # y=0
    if root:
        good_path(root.left,counter)
        x=check_val(root.right,counter,root.val)
        y=check_val(root.left,counter,root.val)
        good_path(root.right,counter)
    # print(x)
    # print(y)


if __name__=="__main__":
    n=node(10)
    edges = [[0,1],[0,2],[2,3],[2,4]]
    vals = [1,3,2,1,3]
    list_vals=[]
    for i in edges:
        # print()
        n.insert(vals[i[0]])
        list_vals.append(vals[i[0]])
        if vals[i[1]] not in list_vals:
            list_vals.append(vals[i[1]])
            n.insert(vals[i[1]])

    
    good_path(n,1)