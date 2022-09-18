import numpy as np
#edges of nodes 
edges_vertices=np.array([[1,2],[1,3],[1,4],[3,5],[3,6],[4,7]])
#xi ti and ki 
#7 3 1
#6 3 2
#7 2 3
#5 3 5
x_i_matrics=np.array([[7,3,1],[6,3,2],[7,2,3],[5,3,5]])
#1 2 1 3 1 4 3 5 3 6 4 7
#number of query ruun
number_of_query=4
#number of nodes in tree 
number_of_nodes=7
#1 0 1 0 0 1 0
engertic_matrix=np.array([1,0,1,0,0,1,0])
find_values=[]
for i in x_i_matrics:
    
    find_values.append(i[0])


def find_sub_set(edges,value,counter,list_of_sub_set):
    # print(value)
    if counter==len(edges_vertices):
        print("list")
        return list_of_sub_set
    # print(edges)
    for i in edges:
        # print(i)
        for j in i:
            
            if j==value:
                # print(j)
                # print(i)
                tmp_list=[]
                tmp_list=list(i)
                if tmp_list in list_of_sub_set:
                    pass
                else:
                    list_of_sub_set.append(tmp_list)
                # value=list_of_sub_set[0]
    value=list_of_sub_set[0][0]

    
    return find_sub_set(edges_vertices,value,counter+1,list_of_sub_set)
def matching_values(list_of_values,index):
    pass

# for j in find_values:
#     list_of_sub_set=[]
make_list=[]

values_of=find_sub_set(edges_vertices,find_values[0],1,make_list)
# print(values_of)
test_check=[]
def append_value(test_check,values_of):
    for i in values_of:
        for j in i:
            if j in test_check:
                pass
            else:
                test_check.append(j)
def calcluate_energy(test_check,engertic_matrix):
    test_check=sorted(test_check)
    for i in range(0,len(sorted(test_check[::]))):
        try:
            # print(test_check[i])
            print(test_check[i],"===>",engertic_matrix[test_check[i]-1])
        except:
            pass
def main():
    calcluate_energy
if __name__=="__main__":
    main()