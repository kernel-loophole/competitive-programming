class TreeAncestor(object):

    def __init__(self, n, parent):
    
        self.n=n
        self.parent=parent 
    def check_fn(n):
        l=list()
        for i in range(0,n):
            l.append(i)
        return l[n]

    def getKthAncestor(self, node, k):
        print(self.parent)

        if k%2==0:
            if k>1:
                # print("k",(node//2-1)-k)
                if self.parent[node//k]<0 or (node//2-1)-k==0:
                    
                    return (node//2-1)-k
                else:
                   
                    return self.parent[node//k]
            else:
                
                #print("j",)
                return self.parent[node//k],(node//2-1)+k

        else:
            if k>1:
                print("l")
                print("ma")
                # print("l",self.parent[node//k-1]-1,(node//2-1)-(k))
                if self.parent[node//k]<0 or (node//2-1)-k==0:
                    # print((node//2-1)-k)
                    # print("none is none ")
                    return (node//2-1)-k
                    
            else:
                # print("p",self.parent[node//k],(node//2-1)+k)
                
                return self.parent[node//k]
        return -1

#         for i in range(0,len(self.parent)):
#             if i==k*2:
#                 if k%2!=0:
#                     print(i)
#                 else:
#                     print(i-1)
            
#             if i==node:
#                 if i==1:
#                     print("0")
#                 else:
                    
#                     # prin
#                     # t(self.parent[i],i,(i-k*2)-k)
#                     if k<=2:
#                         if i>len(self.parent)//2:

#                             print(self.parent[self.parent[i]]+self.parent[i]-1)
#                         else:
#                             print(self.parent[self.parent[i]]+self.parent[i]-k*2)   
#                     else:
#                         print("else")
#                         print(self.parent[self.parent[i]]+self.parent[i]-k*2)
# # Your TreeAncestor object will be instantiated and called as such:
n=7
parent=[-1,0,0,1,1,2,2,3,3,4,4,5,5,6,6]
node=14
k=3
obj = TreeAncestor(n, parent)
param_1 = obj.getKthAncestor(node,k)
print(param_1)