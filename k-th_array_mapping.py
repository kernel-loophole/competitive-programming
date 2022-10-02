class TreeAncestor(object):

    def __init__(self, n, parent):
    
        self.n=n
        self.parent=parent 
    
        

    def getKthAncestor(self, node, k):
        print(self.parent)
        for i in range(0,len(self.parent)):
            if i==node:
                if i==1:
                    print("0")
                else:
                    
                    if i-k*2<0:
                        print("-1")
                    print(self.parent[i],i-k)

                
        


# Your TreeAncestor object will be instantiated and called as such:
n=7
parent=[-1, 0, 0, 1, 1, 2, 2]
node=4
k=2
obj = TreeAncestor(n, parent)
param_1 = obj.getKthAncestor(node,k)